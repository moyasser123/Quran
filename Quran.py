#استعاء المكاتب
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config
css= """
@import url('https://fonts.googleapis.com/css2?family=Marhey:wght@300&display=swap');

#h3{
font-family: 'Marhey', sans-serif;
}

#para{
font-family: 'Marhey', sans-serif;
color: #08088A;
}


"""
@config(css_style=css)
def app():
    put_image('https://mail.balagh.com/upload_list/source/Article/New/%D9%83%D8%AA%D8%A7%D8%A8%20%D8%A7%D9%84%D9%84%D9%87/alqem-fe-al-quran.jpg', width='900px', height='200px')
    put_html("""
        <h3 id='h3'>تطبيق القران الكريم</h3>
        <p id='para'>اهلا بكم في تطبيق القران الكريم</p>
        <ul>
            <li>سماع القران الكريم</li>
            <li>احايث نبويه</li>
            <li>حفظ القران الكريم</li>
        </ul>
        <details id='y'>
            <summary>الاستماع الى القران الكريم</summary>
            <p>-سورة الفاتحة بصوت الشيخ ناصر القطامي-</p>
            <audio controls>
                <source src="https://dl.surah.space/dl/reciter/14/64/001.mp3?h=v8EI-P1rR5JVvE0XwJK-ow&expires=1704862864" type= "audio/mp3">
            </audio>
            <p>-سورة الاخلاص بصوت الشيخ ناصر القطامي-</p>
            <audio controls>
                <source src="https://dl.surah.space/dl/reciter/14/64/112.mp3?h=ioHoncc-fPvED51fJYMdgQ&expires=1704887253" type= "audio/mp3"
            </audio>
        </details>
        <hr>
        <p>جميع الحقوق محفوظه</p>
    """).style('direction:rtl; text-align:right;')

start_server(app, port=2828, debug=True)

