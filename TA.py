import tkinter
from tkinter import ttk
from tkinter import messagebox
import locale

locale.setlocale(locale.LC_ALL, 'id_ID')

#function dan method
#dipanggil ketika nilai pada jml produk berubah
def calculate_total():
    jml = int(jml_spinbox.get())
    HargaProduk = harga_produk_entry.get()
    if HargaProduk:
        total_harga = jml * float(HargaProduk)
        total_harga_label.config( #mengubah sesuai dengan hasil perhitungan
            text="Total Harga: {}".format(locale.format_string("Rp %0.2f", total_harga, grouping=True)))

#dipanggil ketika button pesan sekarang ditekan
def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        # #Pengkondisian
        NamaProduk = nama_produk_entry.get()
        if not NamaProduk:
            tkinter.messagebox.showwarning(title="Error", message="Silahkan isi Nama Produk")
            return
        
        HargaProduk = harga_produk_entry.get()
        if not HargaProduk:
            tkinter.messagebox.showwarning(title="Error", message="Silahkan isi Harga Produk")
            return

        jml = int(jml_spinbox.get())
        if jml == 0:
            tkinter.messagebox.showwarning(title="Error", message="Silahkan isi Jumlah Produk")
            return

        jenis = jenis_combobox.get()
        if not jenis:
            tkinter.messagebox.showwarning(title="Error", message="Silahkan pilih Jenis Produk")
            return

        byr = byr_combobox.get()
        if not byr:
            tkinter.messagebox.showwarning(title="Error", message="Silahkan pilih Metode Pembayaran")
            return

        jasakirim = jasakirim_combobox.get()
        if not jasakirim:
            tkinter.messagebox.showwarning(title="Error", message="Silahkan pilih Metode Pengiriman")
            return

        # Melengkapi alamat
        namapenerima = namapenerima_entry.get()
        if not namapenerima:
            tkinter.messagebox.showwarning(title="Error", message="Silahkan isi Nama Penerima")
            return
        
        alamat = alamat_entry.get()
        nohp = nohp_entry.get()
    
        if alamat:
            if nohp.isdigit():
                total_harga = jml * float(HargaProduk)
                total_harga_label.config(
                    text="Total Harga: {}".format(locale.format_string("Rp %0.2f", total_harga, grouping=True)))

                print("=============BIODATA PEMBELI============")
                print("Nama Penerima        : ", namapenerima)
                print("Alamat Penerima      : ", alamat)
                print("No HP                : ", nohp)
                print("=========BARANG YANG ANDA PESAN=========")
                print("Nama Produk          : ", NamaProduk)
                print("Harga Produk         : ", HargaProduk)
                print("Jenis Produk         : ", jenis)
                print("Jumlah Produk        : ", jml)
                print("Metode Pembayaran    : ", byr)
                print("Metode Pengiriman    : ", jasakirim)
                print("=======================================")
                print("Total Harga          : ", total_harga)
                print("Pesanan Anda Sedang dalam Pengemasan")
                print("=======================================")

                show_popup()  # Menampilkan popup setelah pesanan selesai diisi
                reset_gui()

            else:
                tkinter.messagebox.showwarning(title="Error", message="Tulis dalam Angka pada No Hp")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Silahkan isi Alamat Anda")


#dipanggil ketika button batal di tekan
def cancel_order():
    #menghapus input yang diisi pengguna
    nama_produk_entry.delete(0, tkinter.END)
    harga_produk_entry.delete(0, tkinter.END)
    jenis_combobox.set('')
    jml_spinbox.delete(0, tkinter.END)
    byr_combobox.set('')
    jasakirim_combobox.set('')
    namapenerima_entry.delete(0, tkinter.END)
    alamat_entry.delete(0, tkinter.END)
    nohp_entry.delete(0, tkinter.END)
    total_harga_label.config(text="Total Harga: Rp 0,00") #mengatur ulang

#mengecek no hp berupa angka
def nohp_numeric_input(text):
    if text.isdigit() or text == "":
        if len(text) <= 12:
            return True
        else:
            tkinter.messagebox.showwarning(title="Error", message="No Hp harus terdiri dari 12 angka")
            window.bell()
            return False
    else:
        tkinter.messagebox.showwarning(title="Error", message="Silahkan isi No Hp Anda dengan angka")
        window.bell()
        return False


def harga_numeric_input(text):
    if text.isdigit() or text == "":
        return True
    else:
        tkinter.messagebox.showwarning(title="Error", message="Silahkan isi dengan angka pada Harga Produk")
        window.bell()
        return False

def show_popup():
    tkinter.messagebox.showinfo(title="Terimakasih", message="Terimakasih sudah melakukan pemesanan!")

def reset_gui():
    # Menghapus input yang diisi pengguna
    nama_produk_entry.delete(0, tkinter.END)
    harga_produk_entry.delete(0, tkinter.END)
    jenis_combobox.set('')
    jml_spinbox.delete(0, tkinter.END)
    byr_combobox.set('')
    jasakirim_combobox.set('')
    namapenerima_entry.delete(0, tkinter.END)
    alamat_entry.delete(0, tkinter.END)
    nohp_entry.delete(0, tkinter.END)
    total_harga_label.config(text="Total Harga: Rp 0,00")  # Mengatur ulang

window = tkinter.Tk()
window.title("Toko Online")

# OOP 1 Membuat objek frame dari kelas Frame.
frame = tkinter.Frame(window, bg="beige")
frame.pack()

# Saving User Info

#OOP 1 Membuat objek user_info_frame dari kelas LabelFrame.
user_info_frame = tkinter.LabelFrame(frame, text="Pembelian Produk Online")
user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky="news")

#OOP 1 Membuat objek nama_produk_label dari kelas Label.
nama_produk_label = tkinter.Label(user_info_frame, text="Nama Produk")
nama_produk_label.grid(row=0, column=0)
nama_produk_entry = tkinter.Entry(user_info_frame)
nama_produk_entry.grid(row=1, column=0)

harga_produk_label = tkinter.Label(user_info_frame, text="Harga Produk")
harga_produk_entry = tkinter.Entry(user_info_frame, validate="key")
harga_produk_entry['validatecommand'] = (harga_produk_entry.register(harga_numeric_input), "%P")
harga_produk_label.grid(row=2, column=0)
harga_produk_entry.grid(row=3, column=0)


jenis_label = tkinter.Label(user_info_frame, text="Jenis Produk")
jenis_label.grid(row=0, column=1)
#OOP 1 Membuat objek jenis_combobox dari kelas Combobox yang diberikan oleh modul ttk.
jenis_combobox = ttk.Combobox(user_info_frame,
                             values=["", "Pakaian", "ATK", "Kosmetik", "Elektronik", "Peralatan Rumah Tangga","Aksesoris", "Yang Lainnya"])
jenis_combobox.grid(row=1, column=1)

jml_label = tkinter.Label(user_info_frame, text="Jumlah Produk")
jml_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to=110, command=calculate_total)
jml_label.grid(row=0, column=2)
jml_spinbox.grid(row=1, column=2)

byr_label = tkinter.Label(user_info_frame, text="Metode Pembayaran")
byr_combobox = ttk.Combobox(user_info_frame,
                            values=["COD", "Transfer Bank", "Gopay", "Dana", "Kartu Kredit", "OVO", "Shoope pay"])
byr_label.grid(row=2, column=1)
byr_combobox.grid(row=3, column=1)

jasakirim_label = tkinter.Label(user_info_frame, text="Metode Pengiriman")
jasakirim_combobox = ttk.Combobox(user_info_frame, values=["JNE", "J&T", "Pos Indonesia", "Tiki", "SiCepat"])
jasakirim_label.grid(row=2, column=2)
jasakirim_combobox.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Melengkapi alamat
biodata_frame = tkinter.LabelFrame(frame, text="Biodata Pembeli")
biodata_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

namapenerima_label = tkinter.Label(biodata_frame, text="Nama")
namapenerima_label.grid(row=0, column=0)
namapenerima_entry = tkinter.Entry(biodata_frame)
namapenerima_entry.grid(row=0, column=1)

alamat_label = tkinter.Label(biodata_frame, text="Alamat")
alamat_entry = tkinter.Entry(biodata_frame)
alamat_label.grid(row=1, column=0)
alamat_entry.grid(row=1, column=1)

nohp_label = tkinter.Label(biodata_frame, text="No Hp")
nohp_label.grid(row=2, column=0)
nohp_entry = tkinter.Entry(biodata_frame, validate="key")
nohp_entry['validatecommand'] = (nohp_entry.register(nohp_numeric_input), "%P")
nohp_entry.grid(row=2, column=1)

for widget in biodata_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
ketentuan_frame = tkinter.LabelFrame(frame, text="Syarat & Ketentuan")
ketentuan_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Accepted")
ketentuan_check = tkinter.Checkbutton(ketentuan_frame, text="Barang yang sudah dibeli tidak dapat ditukar kembali",
                                  variable=accept_var, onvalue="Accepted")
ketentuan_check.grid(row=0, column=0)

# Total price label
total_harga_label = tkinter.Label(frame, text="Total Harga: Rp 0,00")
total_harga_label.grid(row=3, column=0, padx=20, pady=10)

# Buttons
order_button = tkinter.Button(frame, text="Pesan Sekarang", command=enter_data, width=70, bg="sky blue")
order_button.grid(row=6, column=0, padx=20, pady=10)

cancel_button = tkinter.Button(frame, text="Batal Order", command=cancel_order, width=15, bg="sky blue")
cancel_button.grid(row=5, column=0, sticky="w", padx=20, pady=10)

window.mainloop()
    

