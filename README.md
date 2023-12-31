# Tugas 2
Adaptable Link:
[Eurora's Closet](https://euroras-closet.adaptable.app)

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    -   Membuat sebuah proyek Django baru

        Untuk membuat sebuah proyek Django baru, pertama-tama saya membuat direktori baru yang saya beri nama ___"inventory"___. Kemudian saya juga membuat repositori baru di GitHub yang nantinya akan dikonfigurasi dengan direktori inventory.

        Setelah itu, saya melakukan inisiasi (git init), konfigurasi global dengan username dan email GitHub (git config --global), menyalin alamat url repositori, dan menghubungkan direktori dengan repositori (git remote add origin)

        Setelah direktori dan repositori saya terhubung, saya mengaktifkan virtual environment agar proyek Django kali ini terisolasi dan tidak terganggu oleh program luar. Kemudian, di dalam direktori saya menambahkan depedencies yang akan mendukung proyek berjalan masing-masing. 

        Depedencies yang saya gunakan mengikuti requirements.txt yang ada pada tutorial. Setelah depedencies diinstall, proyek Django akan terbuat ketika dijalankan perintah `"django-admin startproject inventory ."`.

        Kemudian setelah proyek Django terbuat, muncul beberapa file seperti settings.py dan manage.py. Untuk keperluan deployment, `ALLOWED_HOSTS` pada settings.py saya isi `["*"]` yang artinya mengizinkan semua host. Pada manage.py saya melakukan run server untuk melihat situasi proyek Django pada local host di peramban web. 

    -   Membuat aplikasi dengan nama main pada proyek tersebut

        Saya menjalankan perintah `"python manage.py startapp main"` di dalam direktori untuk memunculkan direktori baru bernama main dan berisi struktur awal aplikasi main. Kemudian menambahkan `"main"` pada settings.py di variabel `INSTALLED_APPS` dan secara otomatis aplikasi main sudah terdaftar di proyek inventory saya.

    -   Melakukan routing pada proyek agar dapat menjalankan aplikasi main

        Dalam direktori inventory, ada berkas urls.py yang saya tambahkan path ke main. Dengan cara mengimpor fungsi include kemudian menambahkan `"path('main/', include('main.urls'))"` di variabel urlpatterns. 

    -   Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib: name sebagai nama item dengan tipe CharField, amount sebagai jumlah item dengan tipe IntegerField, dan description sebagai deskripsi item dengan tipe TextField

        Dalam direktori inventory, ada berkas models.py yang isinya saya atur sebagai berikut:
        ```
        class Item(models.Model):
            name = models.CharField(max_length=100)
            amount = models.PositiveIntegerField()
            description = models.TextField()
            category = models.CharField(max_length=100, null=True, blank=True)
        ```
        Terlihat dalam class Item saya juga menambahkan atribut category dengan tipe CharField.
        Setelah itu, saya melakukan migrasi model agar dapat diaplikasikan ke basis data dengan perintah `"python manage.py makemigrations"` dan `"python manage.py migrate"`.

    -   Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu

        Saya kemudian menambahkan direktori baru bernama templates di dalam direktori main yang berisi berkas main.html yang akan menampilkan nama aplikasi, nama saya, dan kelas saya. Saya kemudian lanjut mengisi berkas tersebut dengan syntax html yang sesuai.
        Setelah itu, dalam views.py di bagian function `show_main` dalam variabel context, saya menambahkan dictionary untuk nama aplikasi, nama saya, dan kelas saya. Kemudian mereturn function tersebut dengan `"return render(request, "main.html", context)"`.

    -   Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py

        Berbeda dengan urls.py di proyek, ada juga urls.py yang memetakan fungsi pada views.py. Saya membuat berkas urls.py baru kemudian menambahkan isinya dengan:
        ```
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```

    -   Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet

        Sebelum mendeploy, saya melakukan testing proyek Django saya terlebih dahulu dan ketika sudah OK maka saya melakukan git add, commit, dan push ke GitHub yang nantinya akan dilakukan deployment.
        Dalam proses mendeploy, saya menggunakan cara dan langkah yang kurang lebih sama seperti yang dicontohkan pada tutorial, hanya saja saya merubah start command menjadi `"python manage.py migrate && gunicorn inventory.wsgi"`.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    ![Bagan](image/bagan.png)

    Client dapat berupa web atau aplikasi yang merequest HTTP ke Django, yang akan berhubungan dengan uRLS yang sudah dipetakan ke fungsi dalam views.py yang sesuai. Kemudian, views.py dan models.py berinteraksi dalam mendefisinikan struktur data proyek Django. HTML file pada templates kemudian akan dirender dan ditampilkan kepada Client melalui HTTP.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Virtual Environment adalah tools dari Python yang memungkinkan pengembang untuk membuat project environment yang "private" atau dalam kata lain terisolasi dari proyek-proyek lainnya. Virtual Environment sangat bermanfaat untuk digunakan,karena penggunaan Virtual Environment bisa memastikan masing-masing proyek memiliki depedencies yang sesuai dan tidak bertabrakan, masing-masing proyek dapat menggunakan versi python yang berbeda, serta dapat memastikan proyek bekerja dengan keinginan pengembang meskipun dijalankan di mesin lain.
    
    Namun, meskipun begitu aplikasi web berbasis Django mungkin saja dibuat tanpa menggunakan Virtual Environment. Tentu saja dengan beberapa konsekuensi seperti terjadinya konflik antarproyek, kesulitan migrasi ketika proyek berpindah tangan, dan alasan keamanan proyek lainnya. Maka dari itu, penggunaan Virtual Environment pada proyek Django merupakan best practice.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    ___MVC___ adalah Model-View-Controller. ___MTV___ adalah Model-Template-View. ___MVVM___ adalah Model-View-ViewModel. Ketiganya adalah pola arsitektur dari pengembangan website atau aplikasi.

    Model pada ketiganya sama-sama mempresentasikan data, berhubungan dengan database, dan akan memperbarui view yang berubah sesuai perubahan data. 

    View merepresentasikan interaksi antarmuka dengan pengguna atau UI. Secara garis besar, View akan mengambil data dari model kemudian menampilkan ke pengguna serta mengirim perintah dari pengguna ke Controller. View ini terdapat pada MVC dan MVVM, namun pada MTV dianalogikan dengan Template. 

    Controller berfungsi menerima input dari pengguna, memproses input, dan mengembalikan output. Controller ini terdapat pada MVC dan dianalogikan sebagai View pada MTV. 

    ViewModel pada MVVM juga sama-sama menangani input dari pengguna dan mengembalikan output, secara khusus menggunakan teknik two-way data binding yang secara otomatis berubah ketika data berubah.

# Tugas 3

1. Apa perbedaan antara form `POST` dan form `GET` dalam Django?

    `GET` digunakan ketika ingin membaca atau mengambil data dari web server, sedangkan `POST` digunakan untuk mengirim form atau data ke server.

    Beberapa perbedaan antara `POST` dan `GET` antara lain:
    
    - `GET` dibatasi panjang stringnya sampai 2047 karakter, sedangkan `POST` tidak.
    - `POST` menginput data melalui form sedangkan `GET` melalui URL
    - `POST` seringkali digunakan untuk mengirim data privat dan sensitif sedangkan `GET` digunakan untuk mengakses data-data biasa 

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

    __HTML__ digunakan untuk mendeskripsikan konten di website secara lengkap dengan representasi visual yang dapat ditentukan oleh pengembang sendiri. Umumnya digunakan untuk menampilkan konten di web saja, tidak untuk pertukaran data.

    __XML__ digunakan untuk merepresentasikan data dengan struktur yang cukup kompleks, yaitu menggunakan opening dan closing tag. Relatif lebih lambat dalam proses pengiriman data karena adanya tag.

    __JSON__ digunakan untuk pertukaran data dan memiliki syntax dictionary dengan `key` dan `value`. Tidak mendukung beberapa atribut dalam HTML dan XML tetapi mudah dan ringkas digunakan dalam pertukaran data.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    JSON banyak digunakan karena dianggap _"human-readable"_ sehingga membantu dan memudahkan Front-End Developer dan Back-End Developer untuk berkomunikasi. JSON juga fleksibel dalam penggunaannya karena mudah untuk direvisi.

    Karena kesederhanaan dan fleksibilitas penggunaannya, JSON sering digunakan dalam pertukaran data antara aplikasi web modern. Kecepatan dan efisiensi pertukaran data merupakan hal yang paling diperhatikan, sehingga penggunaan JSON mempermudah adanya pertukaran data. Selain itu, JSON juga tidak menggunakan memori terlalu banyak jika dibandingkan dengan XML.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    -   Membuat input form untuk menambahkan objek model pada app sebelumnya.
    
        Pertama, yang saya lakukan adalah membuat berkas forms.py di direktori main kemudian menambahkan model untuk form sesuai dengan model Item di models.ppy yang sudah pernah dibuat sebelumnya.

        Pada bagian `fields` saya menambahkan model `name`, `amount`, `description`, dan `category` sesuai dengan model pada models.py saya.
    
        Kemudian saya mengimpor form pada views.py dan membuat function `create_item` yang berfungsi untuk menambahkan item ke tabel inventory. Saya juga menambahkan `items = Item.objects.all()` untuk menampilkan item-item yang pernah ditambahkan. Tidak lupa, menambahkan url di urls.py sebagai path untuk function `create_item`.
    
    -   Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

        Setelah selesai dengan function dan menampilkan item, saya melakukan 4 function lainnya yaitu:
        ```
        show_xml, show_json, show_xml_by_id, show_json_by_id
        ```

        Saya mengatur masing-masing function tersebut seperti yang diajarkan pada tutorial agar objek bisa ditampilkan pada kelima format pada views.py.

    -   Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

        Tidak hanya membuat functionnya, perlu juga masing-masing function tersebut mempunyai routing URL. Sehingga, saya mengatur path untuk kelima format pada urls.py agar tiap format dapat diakses sesuai URLnya masing-masing.

        Sebagai berikut:
        ```
        ...
        path('', show_main, name='show_main'),
        path('create-item', create_item, name='create_item'),
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
        ...
        ```

        Terakhir, setelah semua URL dapat diakses, saya menambahkan beberapa hal seperti merubah tampilan HTML dan menambahkan beberapa informasi.

### Hasil Akses URL pada Postman

#### HTML

![HTML](image/html-postman.png)

#### XML

![XML](image/xml-postman.png)

#### JSON

![JSON](image/json-postman.png)

#### XML by ID

![XML-ID](image/xml-id-postman.png)

#### JSON by ID

![JSON-ID](image/json-id-postman.png)

# Tugas 4
1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

    Django `UserCreationForm` adalah sebuah `form` Django yang digunakan untuk create user baru yang dapat digunakan dalam web app. Umumnya, `UserCreationForm` punya 3 field yaitu: `username`, `password1`, dan `password2`. Field `password2` biasanya digunakan untuk mengonfirmasi password sebelumya.
    
    Kelebihan `UserCreationForm`: Merupakan default `form` dari Django sehingga pengembang Django tidak perlu membuat model form lagi dan dapat langsung disimpan di database. Tampilan `UserCreationForm` juga dapat dilakukan _customization_ sehingga dapat disesuaikan dengan tampilan web app.
    
    Kekurangan `UserCreationForm`:
    Mungkin untuk penambahan field lain dan perubahan tampilan harus dilakukan perubahan sendiri.


2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

    Autentikasi adalah proses verifikasi siapa user yang berusaha menggunakan akses. Sedangkan otorisasi adalah proses verifikasi user yang telah diautentikasi apakah dapat mengakses suatu sistem. Dalam konteks Django, keduanya penting karena berhubungan satu sama lain dalam mengatur administrasi database. 

3. Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?

    _Cookies_ adalah penyimpanan data _client_ yang sifatnya sementara (hanya tersimpan ketika pengguna sedang melakukan interaksi di dalam aplikasi web). Dalam Django, _cookies_ dikelola dengan struktur seperti map yang terdiri dari key dan value berupa user dan data yang disimpan. Untuk menjaga keamanan data, pada Django juga terdapat _expiration date_ sehingga ketika pengguna sudah keluar dari aplikasi web, data-data pengguna juga akan dinonaktifkan.

4. Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

    _Cookies_ disimpan pada sisi _client_, sehingga keamanan sebenarnya tergantung pada _browser_ milik _client_. _Cookies_ juga dapat dilihat secara langsung oleh pengguna sehingga sebenarnya tidak aman jika digunakan untuk menyimpan sesuatu yang sifatnya _private_. 

    Beberapa resiko potensial yang harus diwaspadai terhadap keamanan _cookies_ adalah adanya ___Cookie Theft___ yaitu pencurian _cookies_ karena mendapat akses ilegal ke _cookies_ pengguna. Umumnya menyerang informasi pengguna yang bersifat _private_ seperti ID, _validation token_, dan lain-lain sehingga sesi pengguna dapat diambil alih.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

        Untuk mengimplementasikan fungsi registrasi, login, dan logout, saya menambahkan beberapa fitur django ke views.py yaitu:

        ```
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  
        from django.contrib.auth import authenticate, login, logout
        from django.contrib.auth.decorators import login_required
        ```
        Setelah mengimpor, saya juga mendefinisikan masing-masing functionnya, seperti `register(request)`, `login_user(request)`, dan `logout_user(request)`. Tidak lupa saya juga mengatur bagian `login_required` serta menghubungkan fungsi login dan logout pada cookie.
        
        Kemudian saya menyambungkannya ke file urls.py untuk setiap path register, login, dan logout.

    - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

        Untuk menguji coba, saya menjalankan program pada localhost dan memanfaatkan fungsi register untuk mendaftarkan 2 akun baru. Kemudian, untuk masing-masing akun yang telah dibuat, saya menerapkan fungsi login, menambahkan masing-masing 3 _dummy_ data, dan menerapkan fungsi logout.

    - Menghubungkan model Item dengan User.

        Dalam menghubungkan model Item dengan User, pertama-tama yang saya lakukan adalah mengimpor `from django.contrib.auth.models import User` ke dalam models.py. Setelah itu, pada model Item saya tambahkan kode:
        `user = models.ForeignKey(User, on_delete=models.CASCADE)` serta mengubah kode di views.py untuk `create_item` dan `show_main` sebagai berikut:

        ```
        @login_required(login_url='/login')
        def show_main(request):
        items = Item.objects.all()

        last_login = request.COOKIES.get('last_login', 'Not available')    

        context = {
            'app_name': "EURORA'S CLOSET",
            'name': request.user.username,
            'class': 'PBP A',
            'items': items,
            'last_login': last_login,
        }

        return render(request, "main.html", context)

        def create_item(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_item.html", context)
        ```
        Maka dengan ini, sudah terhubung dengan _cookie_ dan _context_ akan disesuaikan ke dalam HTML file. Kemudian terakhir adalah melakukan _migrations_ untuk mengatur perubahan. 

    - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

        Karena sebelumnya, saya sudah mengatur _cookie_ maka informasi pengguna yang sedang _logged in_ dan _last login_ hanya perlu diatur pada file HTML dengan menambahkan:
        ```
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        ```

# Tugas 5
 1. Jelaskan manfaat dari setiap _element selector_ dan kapan waktu yang tepat untuk menggunakannya.

    _Elemen selector_ adalah sebuah instruksi CSS yang mengelompokkan elemen sehingga elemen tersebut memiliki _style_ yang sama. Contohnya:
    ```
    h5 {
        text-align: center;
        color: yellow;
    }
    ```
    Sehingga, dengan pengaturan elemen, semua elemen h5 akan memiliki _center text alignment_ dan warna _yellow_.

    _Elemen selector_ akan tepat digunakan ketika ingin membuat spesifikasi untuk suatu elemen agar dalam 1 file html, semua elemen tersebut memiliki _style_ yang sama dan konsisten. Contohnya adalah ketika ingin mengatur warna dan _font_ untuk _heading_ tertentu.
    
 2. Jelaskan HTML5 Tag yang kamu ketahui.

    Berikut adalah beberapa HTML5 Tag yang saya ketahui:
    ```
    - <a> : untuk mengarahkan ke suatu tautan
    - <body> : untuk mendefinisikan body dari file
    - <br> : untuk membuat line break
    - <button> : untuk membuat sebuah tombol yang dapat diclick
    - <div> : untuk mendefinisikan per-bagian
    - <head> : untuk mendefinisikan heading dari file
    - <hr> : untuk membuat sebuah garis horizontal
    - <img> : untuk input sebuah foto
    - <li> : untuk membuat daftar item
    - <table> : untuk membuat table data, ada juga yang termasuk di dalamnya seperti <tr>, <th>, <td>
    - dan masih banyak tag lainnya.
    ```

 3. Jelaskan perbedaan antara margin dan padding.

    Margin adalah area kosong pada bagian terluar sebuah file. Margin dihitung dari bagian terluar file dan bentuknya adalah transparan. 
    
    Sedangkan padding adalah area kosong pada bagian luar sebuah konten. Padding dihitung dari bagian terluar konten dan bentuknya juga transparan. 

    Perbedaan utamanya terletak pada posisinya yaitu, margin relatif ada di bagian paling luar sedangkan padding menyelimuti sebuah konten.

 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

    | Bootstrap | Tailwind | 
    | :--------: | :--------: |
    | Bootstrap memiliki komponen-komponen design yang siap digunakan | Tailwind memiliki design yang bisa dikombinasikan dengan kelas utilitas |
    | Ukuran file CSS Bootstrap umumnya lebih besar | Ukuran file CSS Tailwind umumnya lebih kecil dibandingkan Bootstrap |
    | Penggunaan Bootstrap akan menyeragamkan design website | Penggunaan Tailwind dapat disesuaikan dengan setiap project karena lebih fleksibel |
    | Bootstrap kerap digunakan untuk pemula | Tailwind perlu dipelajari lebih lanjut |

    Bootstrap tepat untuk digunakan bagi pemula yang ingin hasil maksimal tanpa perlu banyak menyesuaikan diri dengan kesulitan menggunakan CSS, karena bootstrap sudah menyediakan semua komponen CSS yang siap digunakan. Selain itu, _design_ bootstrap cenderung lebih konsisten.

    Sedangkan Tailwind tepat digunakan bagi pengembang web yang ingin memiliki spesifikasi tersendiri bagi _design_ webnya tersebut. Tailwind juga menyediakan kelas _utility_ untuk _design-design_ yang lebih kompleks.

 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 -  Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.

    Pada halaman login dan register, saya membuat halaman tersebut lebih menarik dengan mengatur _alignment_ untuk _form_ _username_ dan _password_ rata tengah sehingga lebih nyaman dilihat.

    Sedangkan untuk file _main_ saya membuat _design_ yang sesuai dengan _branding_ dan karakteristik yang saya ingin kembangkan sesuai aplikasi saya.
 
 - Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

    Saya menggunakan bootstrap CSS untuk membuat _item_ pada inventori saya dengan Card. Saya membuat Card untuk setiap _item_ yang diinput pada halaman daftar inventori. Card ini akan sekaligus menggantikan tabel yang sebelumnya menampilkan daftar item.

# Tugas 6
### Link URL Tugas: [Eurora's Closet](http://lidwina-eurora-tugas.pbp.cs.ui.ac.id)

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

    _Asynchronous programming_ artinya setiap eksekusi _task_ dapat dilakukan tanpa perlu menunggu _task_ sebelumnya selesai. _Asynchronous programming_ memungkinkan eksekusi secara paralel dan meningkatkan responsivitas program dengan waktu yang lebih singkat.

    Sedangkan _synchronous programming_ artinya setiap eksekusi _task_ harus berurutan, yakni setiap _task_ yang akan dieksekusi harus menyelesaikan _task_ sebelumnya dahulu. _Synchronous programming_ membuat _flow_ program menjadi lebih mudah dipahami karena linear, namun jika dibandingkan dengan _asynchronous programming_ dapat memakan waktu yang lebih lama.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

    Paradigma _event-driven programming_ mengacu pada waktu sebuah task dieksekusi yang ditentukan oleh suatu _event_ tertentu. Program dengan _event-driven_ dapat mengeksekusi sebuah task secara langsung tanpa perlu menjalankan kode-kode di urutan seelumnya. Dalam _event-driven programming_ terdapat _event handler_ yang berfungsi untuk mendefinisikan respons program ketika _event_ terjadi.

    Contoh penggunaannya dalam JavaScript dan AJAX pada project saya adalah:
    `document.getElementById("saveItemButton").addEventListener("click", addItem)`
    Kode di atas berarti bahwa ketika _button_ Save Item di-_click_, maka Item akan bertambah sesuai dengan fungsi `addItem`.

3. Jelaskan penerapan asynchronous programming pada AJAX.

    AJAX merupakan singkatan dari Asynchronous JavaScript And XML, yang artinya AJAX menggunakan _asynchronous programming_ untuk dapat bekerja. Untuk memberi tanda bahwa sebuah fungsi transfer data menggunakan AJAX beroperasi secara _asynchronous programming_, maka fungsi tersebut dapat menggunakan kata kunci `async`.
    
    Kemudian, untuk memastikan bahwa kode program lainnya akan tetap berjalan dengan lancar sementara server mengolah _input_ dan mengirimkan _output_ AJAX, maka dapat digunakan `fetch()` untuk melakukan HTTP GET Request dan Await. Ketika respons yang sudah selesai dieksekusi sudah diterima, maka kemudian fungsi-fungsi yang sudah didefinisikan pada JavaScript akan diproses dalam program.

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

    | Fetch API | Library jQuery | 
    | :--------: | :--------: |
    | Tidak memerlukan library tambahan | Merupakan sebuah library tambahan yang perlu diinstall terlebih dahulu |
    | Menangani respons dan _error_ dengan lebih mudah dibaca karena menggunakan _promises_ | Terdapat versi jQuery yang masih menggunakan _callback_, yang terbilang cukup sulit dibandingkan _promises_ |
    | Instruksi yang ada lebih sederhana | Memiliki lebih banyak _plugin_ yang memudahkan beberapa tugas |
    | Cocok untuk _browser_ modern, namun tidak untuk beberapa _browser_ lama | Lebih _compatible_ untuk semua _browser_ (_cross-browser_) karena dapat menyesuaikan perbedaan pada tiap _browser_ |

    Menurut saya, Fetch API dan Library jQuery memiliki kelebihan dan kekurangannya masing-masing. Namun, untuk _project_ sederhana seperti _inventory_ ini lebih mudah untuk menerapkan AJAX dengan Fetch API. Selain tidak memerlukan _library_ eksternal, secara khusus _project_ yang sedang dibuat merupakan _project_ yang didukung pada _browser_ modern dan tidak memerlukan terlalu banyak fitur lain pada jQuery.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Mengubah AJAX GET

    Dalam mengimplementasikan AJAX GET, pertama-tama saya membuat fungsi `get_item_json` yang tugasnya adalah untuk melakukan _fetch_ dari berkas main.html, mengambil data input item dari _user_, kemudian mengembalikan data tersebut menggunakan format JSON. Saya juga melakukan _routing_ fungsi tersebut ke dalam views.py.

    Ketika `get_item_json` dieksekusi, harapan saya adalah data pada daftar card akan ter-_update_. Untuk meng-_update_ tampilan card, saya membuat `async function refreshItems()` yang akan me-_refresh_ Item secara otomatis ketika dieksekusi.

- Mengubah AJAX POST

    Dalam mengimplementasikan AJAX POST, saya memanfaatkan tutorial yaitu membuat sebuah _button_ yang akan membuka sebuah modal. Modal yang ada pada tutorial saya modifikasi sesuai dengan _models_ yang digunakan dalam _project_ saya. Namun, sebelumnya saya membuat fungsi `add_item_ajax` untuk menambahkan Item baru dan menyimpan Item tersebut ke dalam _database_. Tidak lupa, saya melakukan _routing_ fungsi tersebut ke dalam views.py.

    Selain itu, dalam berkas main.html saya juga menambahkan `async function addItem()` yang berfungsi untuk melakukan fetch dan mengirimkan HTTP Request sesuai dengan paradigma _event-driven programming_ yang akan dieksekusi ketika button pada modal di-_click_.

- Melakukan perintah `collectstatic`

    Untuk melakukan `collectstatic`, saya menambahkan kode di bawah ini pada berkas settings.py:
    ```
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ```

    Kemudian, saya menjalankan `python manage.py collectstatic` di terminal untuk mengumpulkan _file static_ dari setiap aplikasi saya.