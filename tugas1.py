"""
buat program sederhana untuk mengisi sebuag data dictionary.
datanya :
-Nama
-Umur
-Pekerjaan
-Salary

output:
dictionary
{"Nama":"Uno", "Umur":36, "pekerjaan":"Ngajar", "Salary":100000000}
"""
Nama = input("masukan nama:")
Umur = input("masukan umur:")
Pekerjaan = input("masukan pekerjaan:")
Salary = input("masukan salary:")
data_dict = {"Nama":Nama,"Umur":Umur, "pekerjaan":"Pekerjaan", "Salary":Salary}
print(data_dict)