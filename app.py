from flask import Flask, render_template, request, url_for, redirect,flash
from flask_mysqldb import MySQL
app = Flask(__name__)
app.secret_key = "#yamatekudasai#"
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'trending'
mysql = MySQL(app)

@app.route("/")
def indexku():
    return render_template('index.html')

@app.route('/masterbarang')
def masterbarang():
 cur = mysql.connection.cursor()
 cur.execute("SELECT * FROM masterbarang")
 barang = cur.fetchall()
 cur.close() 
 return render_template('masterbarang.html',menu='master',submenu='barang', data = barang)

@app.route("/formmasterbarang")
def formmasterbarang():
   return render_template('formmasterbarang.html')

@app.route('/simpanformmasterbarang', methods=["GET", "POST"])
def simpanformmasterbarang():
 if request.method == 'GET': return render_template('formmasterbarang.html')
 else:
    nama = request.form['nama']
    harga = request.form['harga']
    satuan = request.form['satuan']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO masterbarang (nama,harga,satuan) VALUE (%s,%s,%s)", (nama,harga,satuan))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('masterbarang'))
 
@app.route('/edit/formmasterbarang/<int:id>', methods=["GET", "POST"])
def editformmasterbarang(id):
  if request.method == 'GET':
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM masterbarang WHERE id=%s", (id, ))
    barang = cur.fetchone()
    cur.close()
    return render_template('formeditmasterbarang.html', data=barang)
  else:
    nama = request.form['nama']
    harga = request.form['harga']
    satuan = request.form['satuan']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE masterbarang SET nama=%s, harga=%s, satuan=%s WHERE id=%s;" ,(nama,harga,satuan,id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('masterbarang'))
  
@app.route('/delete/masterbarang/<int:id>', methods=["GET"])
def deletemasterbarang(id):
 if request.method == 'GET':
   cur = mysql.connection.cursor()
   cur.execute("DELETE FROM masterbarang where id = %s", (id,))
   mysql.connection.commit()
   cur.close()
   return redirect(url_for('masterbarang'))
 
@app.route('/masterpelanggan')
def masterpelanggan():
 cur = mysql.connection.cursor()
 cur.execute("SELECT * FROM masterpelanggan")
 pelanggan = cur.fetchall()
 cur.close() 
 return render_template('masterpelanggan.html',menu='master',submenu='pelanggan', data = pelanggan)

@app.route("/formmasterpelanggan")
def formmasterpelanggan():
   return render_template('formmasterpelanggan.html')

@app.route('/simpanformmasterpelanggan', methods=["GET", "POST"])
def simpanformmasterpelanggan():
  if request.method == 'GET':
    return render_template('formmasterpelanggan.html')
  else: 
    nama = request.form['nama']
    alamat = request.form['alamat']
    kota = request.form['kota']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO masterpelanggan (nama,alamat,kota) VALUE (%s,%s,%s)", (nama,alamat,kota))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('masterpelanggan'))
  
@app.route('/edit/formmasterpelanggan/<int:id>', methods=["GET", "POST"])
def editformmasterpelanggan(id):
  if request.method == 'GET':
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM masterpelanggan WHERE id=%s", (id, ))
    pelanggan = cur.fetchone()
    cur.close()
    return render_template('formeditmasterpelanggan.html', data=pelanggan)
  else:
    nama = request.form['nama']
    alamat = request.form['alamat']
    kota = request.form['kota']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE masterpelanggan SET nama=%s, alamat=%s, kota=%s WHERE id=%s;" ,(nama,alamat,kota,id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('masterpelanggan'))
  
@app.route('/delete/masterpelanggan/<int:id>', methods=["GET"])
def deletemasterpelanggan(id):
  if request.method == 'GET':
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM masterpelanggan where id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('masterpelanggan'))

@app.route('/mastersupplier')
def mastersupplier():
 cur = mysql.connection.cursor()
 cur.execute("SELECT * FROM mastersupplier")
 supplier = cur.fetchall()
 cur.close() 
 return render_template('mastersupplier.html',menu='master',submenu='supplier', data = supplier)

@app.route("/formmastersupplier")
def formmastersupplier():
   return render_template('formmastersupplier.html')

@app.route('/simpanformmastersupplier', methods=["GET", "POST"])
def simpanformmastersupplier():
  if request.method == 'GET':
    return render_template('formmasterpelanggan.html')
  else: 
    nama = request.form['nama']
    alamat = request.form['alamat']
    kota = request.form['kota']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO mastersupplier (nama,alamat,kota) VALUE (%s,%s,%s)", (nama,alamat,kota))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('mastersupplier'))
  
@app.route('/edit/formmastersupplier/<int:id>', methods=["GET", "POST"])
def editformmastersupplier(id):
  if request.method == 'GET':
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mastersupplier WHERE id=%s", (id, ))
    supplier = cur.fetchone()
    cur.close()
    return render_template('formeditmastersupplier.html', data=supplier)
  else:
    nama = request.form['nama']
    alamat = request.form['alamat']
    kota = request.form['kota']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE mastersupplier SET nama=%s, alamat=%s, kota=%s WHERE id=%s;" ,(nama,alamat,kota,id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('mastersupplier'))
  
@app.route('/delete/mastersupplier/<int:id>', methods=["GET"])
def deletemastersupplier(id):
  if request.method == 'GET':
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM mastersupplier where id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Data delete successfully','success')
    return redirect(url_for('mastersupplier'))
  
@app.route('/datapembelian')
def datapembelian():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `datapembelian`")
    data = cur.fetchall()
    cur.close()
    
    rows = []
    for row in data:
        cur = mysql.connection.cursor()
        cur.execute("SELECT harga FROM masterbarang WHERE nama = %s ", (row[3],))
        kharga = cur.fetchone()
        cur.close()

        if kharga is not None :
          harga = kharga[0]
          total_harga = int(row[5]) * int(harga)
          rows.append((row[0], row[1], row[2], row[3], harga, row[5], total_harga))
    return render_template("datapembelian.html", data=rows)

@app.route("/formpembelian", methods=["GET", "POST"])
def formdatapembelian():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT DISTINCT nama FROM mastersupplier")
        sup = cur.fetchall()
        options = [row[0] for row in sup]
        cur.execute("SELECT DISTINCT nama FROM masterbarang")
        barang = cur.fetchall()
        optionso = [row[0] for row in barang]
        cur.execute("SELECT DISTINCT harga FROM masterbarang")
        barangg = cur.fetchall()
        optionss = [row[0] for row in barangg]
        cur.close()
        return render_template("formdatapembelian.html", options=options, optionso=optionso, total=optionss)

@app.route('/simpanformdatapembelian', methods=["GET", "POST"])
def simpanformdatapembelian():
  if request.method == 'GET':
    return render_template('formdatapembelian.html')
  else: 
    tanggal = request.form['tanggal']
    supplier = request.form['supplier']
    barang = request.form['barang']
    item = request.form['item']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO datapembelian (tanggal,supplier,barang,item) VALUE (%s,%s,%s,%s)", (tanggal,supplier,barang,item))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('datapembelian'))
  
  
@app.route('/delete/datapembelian/<int:id>', methods=["GET"])
def deletedatapembelianr(id):
  if request.method == 'GET':
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM datapembelian where id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Data delete successfully','success')
    return redirect(url_for('datapembelian'))
  

@app.route('/datapenjualan')
def datapenjualan():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM datapenjualan")
    data = cur.fetchall()
    cur.close
  
    rows = []
    for row in data:
        cur = mysql.connection.cursor()
        cur.execute("SELECT harga FROM masterbarang WHERE nama = %s ", (row[3],))
        kharga = cur.fetchone()

        if kharga is not None :
          harga = kharga[0]
          cur.close()
          total_harga = int(row[5]) * int(harga)
          rows.append((row[0], row[1], row[2], row[3], harga, row[5], total_harga))
    return render_template("datapenjualan.html", data=rows)

@app.route("/formpenjualan", methods=["GET", "POST"])
def formdatapenjualan():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT DISTINCT nama FROM masterpelanggan")
        sup = cur.fetchall()
        options = [row[0] for row in sup]
        cur.execute("SELECT DISTINCT nama FROM masterbarang")
        barang = cur.fetchall()
        optionso = [row[0] for row in barang]
        cur.close()
        return render_template("formdatapenjualan.html", options=options, optionso=optionso)
    

@app.route('/simpanformdatapenjualan', methods=["GET", "POST"])
def simpanformdatapenjualan():
  if request.method == 'GET':
    return render_template('formpenjualan.html')
  else: 
    tanggal = request.form['tanggal']
    nama_pelanggan = request.form['nama_pelanggan']
    nama_barang = request.form['nama_barang']
    jumlah = request.form['jumlah']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO datapenjualan (tanggal,nama_pelanggan,nama_barang,jumlah) VALUE (%s,%s,%s,%s)", (tanggal,nama_pelanggan,nama_barang,jumlah))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('datapenjualan'))


@app.route('/edit/formpenjualan/<int:id>', methods=["GET", "POST"])
def editformdatapenjualan(id):
  if request.method == 'GET':
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM datapenjualan WHERE id=%s", (id, ))
    penjualan = cur.fetchone()
    cur.close()
    return render_template('formeditdatapenjualan.html', data=penjualan)
  else:
    tanggal = request.form['tanggal']
    nama_pelanggan = request.form['nama_pelanggan']
    nama_barang = request.form['nama_barang']
    jumlah = request.form['jumlah']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE datapenjualan SET tanggal=%s, nama_pelanggan=%s, nama_barang=%s,jumlah=%s WHERE id=%s;" ,(tanggal,nama_pelanggan,nama_barang,jumlah,id))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('datapenjualan'))

@app.route('/delete/datapenjualan/<int:id>', methods=["GET"])
def deletedatapenjualan(id):
  if request.method == 'GET':
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM datapenjualan where id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    flash('Data delete successfully','success')
    return redirect(url_for('datapenjualan'))


if __name__=='__main__':
    app.run(debug=True)
