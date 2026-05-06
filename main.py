import sys
import pyodbc
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
from Ui.admin import Ui_MainWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # State Awal UI
        self.ui.sidebar_sm.hide()  
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.master_bandara_big.setChecked(True)
        self.load_negara()
        self.ui.simpanmb.clicked.connect(self.simpan_data)

        # Mapping Button untuk Navigasi Sidebar
        menu_mapping = {
            self.ui.master_bandara_big: 0,
            self.ui.masterMaskapai_big: 1,
            self.ui.masterjp_big: 2,
            self.ui.masterkp_big: 3,
            self.ui.ubahsp_big: 4
        }

        for btn, index in menu_mapping.items():
            btn.clicked.connect(lambda checked, i=index: self.ui.stackedWidget.setCurrentIndex(i))

        # Hubungkan tombol simpan ke fungsi simpan_data
        self.ui.simpanmb.clicked.connect(self.simpan_data) # Ganti simpanButton dengan nama objek tombol kamu

        # Konfigurasi Table Widget dan load Data
        self.setup_table_style()
        self.load_data_to_dashboard()

    def get_db_connection(self):
        conn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-PO8UJSH\\SQLEXPRESS;"
            "Database=BromoAirlines;"
            "Trusted_Connection=yes;"
        )
        return pyodbc.connect(conn_str)
    
    def load_negara(self):
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()

            query = """
            SELECT Nama FROM Negara ORDER BY Nama ASC
            """
            cursor.execute(query)

            rows = cursor.fetchall()
            negara_list = [row[0] for row in rows]

            self.ui.comboBox_2.addItems(negara_list)

            conn.close()

        except Exception as e:
            print(f"Gagal Memuat Data Negara: {e}")

    def setup_table_style(self):
        # Sesuai gambar, ada 6 kolom data + 1 kolom aksi (Ubah & Hapus)
        self.ui.masterBandaratable.setColumnCount(7) 
        self.ui.masterBandaratable.setHorizontalHeaderLabels(
            ["Nama", "KodeIATA", "Kota", "Negara", "Terminal", "Alamat", "Aksi"]
        )
        header = self.ui.masterBandaratable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        # Tambahkan state untuk melacak apakah sedang Edit atau Simpan Baru
        self.is_edit_mode = False
        self.current_edit_iata = None

    def load_data_to_dashboard(self):
        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            query = """
                SELECT B.Nama, B.KodeIATA, B.Kota, N.Nama, B.JumlahTerminal, B.Alamat
                FROM Bandara B
                JOIN Negara N ON N.ID = B.NegaraID
                ORDER BY B.Nama ASC
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            self.ui.masterBandaratable.setRowCount(len(rows))

            for row_idx, row_data in enumerate(rows):
                # Isi kolom data (0-5)
                for col_idx, value in enumerate(row_data):
                    self.ui.masterBandaratable.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

                # Kolom 6: Tambahkan Tombol Ubah dan Hapus
                btn_widget = QWidget()
                layout = QHBoxLayout(btn_widget)
                layout.setContentsMargins(2, 2, 2, 2)
                
                btn_ubah = QPushButton("Ubah")
                btn_hapus = QPushButton("Hapus")
                
                # Gunakan lambda dengan default value (r=row_data) agar menangkap data yang benar
                btn_ubah.clicked.connect(lambda ch=None, r=row_data: self.prepare_update(r))
                btn_hapus.clicked.connect(lambda ch=None, k=row_data[1]: self.hapus_data(k))
                
                layout.addWidget(btn_ubah)
                layout.addWidget(btn_hapus)
                self.ui.masterBandaratable.setCellWidget(row_idx, 6, btn_widget)

            conn.close()
        except Exception as e:
            print(f"Gagal Memuat Data: {e}")

    def prepare_update(self, data):
        # Isi form dengan data dari baris yang dipilih
        self.ui.inputNama.setText(data[0])
        self.ui.inputiata.setText(data[1])
        self.ui.inputKota.setText(data[2])
        self.ui.comboBox_2.setCurrentText(data[3])
        self.ui.terminalDropdown.setValue(data[4])
        self.ui.inputAlamat.setPlainText(data[5])
        
        # Set state ke Edit Mode
        self.is_edit_mode = True
        self.current_edit_iata = data[1] # Simpan IATA lama sebagai kunci Update
        print(f"Mode Edit Aktif: Mengubah {data[1]}")

    def hapus_data(self, kode_iata):
        # Tambahkan konfirmasi sesuai dokumentasi image_af34ee.png
        from PySide6.QtWidgets import QMessageBox
        reply = QMessageBox.question(self, "Konfirmasi", f"Apakah Anda yakin ingin menghapus data {kode_iata}?",
                                     QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            try:
                conn = self.get_db_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Bandara WHERE KodeIATA = ?", (kode_iata,))
                conn.commit()
                conn.close()
                self.load_data_to_dashboard()
                print("Data Berhasil Dihapus")
            except Exception as e:
                print(f"Gagal Dihapus: {e}")

    def simpan_data(self):
        nama = self.ui.inputNama.text()
        kode_iata = self.ui.inputiata.text()
        kota = self.ui.inputKota.text()
        negara = self.ui.comboBox_2.currentText()
        jumlah_terminal = self.ui.terminalDropdown.value()
        alamat = self.ui.inputAlamat.toPlainText()

        if not all([nama, kode_iata, kota, alamat]):
            print("Peringatan: Semua data harus diisi!")
            return

        try:
            conn = self.get_db_connection()
            cursor = conn.cursor()

            if self.is_edit_mode:
                # Logika UPDATE
                query = """
                UPDATE Bandara SET Nama=?, KodeIATA=?, Kota=?, 
                NegaraID=(SELECT ID FROM Negara WHERE Nama=?), 
                JumlahTerminal=?, Alamat=? 
                WHERE KodeIATA=?
                """
                cursor.execute(query, (nama, kode_iata, kota, negara, jumlah_terminal, alamat, self.current_edit_iata))
                print("Data Berhasil Diperbarui")
            else:
                # Logika INSERT
                query = """
                INSERT INTO Bandara (Nama, KodeIATA, Kota, NegaraID, JumlahTerminal, Alamat)
                VALUES (?, ?, ?, (SELECT ID FROM Negara WHERE Nama=?), ?, ?)
                """
                cursor.execute(query, (nama, kode_iata, kota, negara, jumlah_terminal, alamat))
                print("Data Berhasil Disimpan")

            conn.commit()
            conn.close()
            
            # Kembalikan form ke kondisi semula (Reset)
            self.is_edit_mode = False
            self.load_data_to_dashboard()
            self.clear_form()
            
        except Exception as e:
            print(f"Kesalahan Database: {e}")

    def clear_form(self):
        self.ui.inputNama.clear()
        self.ui.inputiata.clear()
        self.ui.inputKota.clear()
        self.ui.inputAlamat.clear()
        self.ui.terminalDropdown.setValue(2)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())