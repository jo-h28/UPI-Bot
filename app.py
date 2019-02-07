# mybot/app.py
import datetime
import os
from decouple import config
from flask import (
	Flask, request, abort
)
from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage,
	SourceUser, SourceGroup, SourceRoom,
	TemplateSendMessage, ConfirmTemplate, MessageAction,
	ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
	PostbackAction, DatetimePickerAction,
	CameraAction, CameraRollAction, LocationAction,
	CarouselTemplate, CarouselColumn, PostbackEvent,
	StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
	ImageMessage, VideoMessage, AudioMessage, FileMessage,
	UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
	FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
	TextComponent, SpacerComponent, IconComponent, ButtonComponent,
	SeparatorComponent, QuickReply, QuickReplyButton, DatetimePickerTemplateAction,
)
app = Flask(__name__)
# get LINE_CHANNEL_ACCESS_TOKEN from your environment variable
line_bot_api = LineBotApi(
	config("LINE_CHANNEL_ACCESS_TOKEN",
		   default=os.environ.get('LINE_ACCESS_TOKEN'))
)
# get LINE_CHANNEL_SECRET from your environment variable
handler = WebhookHandler(
	config("LINE_CHANNEL_SECRET",
		   default=os.environ.get('LINE_CHANNEL_SECRET'))
)
# temp for add to do list string
toDoListString = ""

# list mata kuliah
matkul_list = ["IF3110 WBD Pengembangan Aplikasi Berbasis Web", \
"IF3130 JarKom Jaringan Komputer", \
"IF3140 MBD Manajemen Basis Data", \
"IF3150 MPPL Manajemen Proyek Perangkat Lunak", \
"IF3151 IMK Interaksi Manusia dan Komputer", \
"IF3170 AI Intelegensi Buatan"]

@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']


	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)


	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)


	return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
	if (event.message.text.lower() == "nilai"):
		# jika tombol nilai ditekan
		# fungsi yang akan dilakukan ditulis dibawah ini
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Nilai dari mata kuliah apa yang ingin ditampilkan?'))
		menuNilai = CarouselTemplate(
			columns=[
				CarouselColumn(
					title='AI', text='Inteligensi Buatan', defaultAction=MessageAction(label='Lihat Nilai', text='AI'),
					actions=[MessageAction(label='Lihat Nilai', text='AI')]
				),
				CarouselColumn(
					title='Jarkom', text='Jaringan Komputer', defaultAction=MessageAction(label='Lihat Nilai', text='Jarkom'),
					actions=[MessageAction(label='Lihat Nilai', text='Jarkom')]
				),
				CarouselColumn(
					title='IMK', text='Interaksi Manusia Komputer', defaultAction=MessageAction(label='Lihat Nilai', text='IMK'),
					actions=[MessageAction(label='Lihat Nilai', text='IMK')]
				),
				CarouselColumn(
					title='MPPL', text='Manajemen Proyek Perangkat Lunak', defaultAction=MessageAction(label='Lihat Nilai', text='MPPL'),
					actions=[MessageAction(label='Lihat Nilai', text='MPPL')]
				),
				CarouselColumn(
					title='WBD', text='Web-Based Development', defaultAction=MessageAction(label='Lihat Nilai', text='WBD'),
					actions=[MessageAction(label='Lihat Nilai', text='WBD')]
				),
				CarouselColumn(
					title='MBD', text='Manajemen Basis Data', defaultAction=MessageAction(label='Lihat Nilai', text='MBD'),
					actions=[MessageAction(label='Lihat Nilai', text='MBD')]
				)
			]
		)
		messageNilai = TemplateSendMessage(alt_text='Tampilkan Nilai', template=menuNilai)
		line_bot_api.reply_message(event.reply_token, messageNilai)
	elif (event.message.text.lower() == "ai"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Inteligensi Buatan\n' \
		'== KUIS == \n' \
		'Kuis 1 : 75 \n' \
		'Kuis 2 : 88 \n' \
		'== TUGAS == \n' \
		'Tucil 1 : 100 \n' \
		'Tubes 1 : 100 \n' \
		'== UJIAN == \n' \
		'UTS : 99'))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Selamat! Kamu benar-benar bersinar dalam mata kuliah ini!'))
	elif (event.message.text.lower() == "jarkom"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Jaringan Komputer\n' \
		'== KUIS == \n' \
		'Kuis 1 : 90 \n' \
		'Kuis 2 : 101 \n' \
		'Kuis 3 : 85 \n' \
		'Kuis 4 : 95 \n' \
		'Kuis 5 : 90'))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Kuis dadakan bukan menjadi penghalang untuk kamu terus berkembang!'))
	elif (event.message.text.lower() == "imk"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Interaksi Manusia Komputer\n' \
		'== KUIS == \n' \
		'Kuis 1 : 45 \n' \
		'Kuis 2 : 60 \n' \
		'Kuis 3 : 75 \n' \
		'Kuis 4 : 70 \n' \
		'Kuis 5 : 90 \n' \
		'== TUGAS == \n' \
		'Tugas 1 : 95 \n' \
		'Tugas 2 : 85 \n' \
		'Tugas 3 : 80 \n' \
		'Tugas 4 : 90 \n' \
		'Tugas 5 : 95'))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Nilai kuismu kian hari kian membaik! Pertahankanlah!'))
	elif (event.message.text.lower() == "mppl"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Manajemen Proyek Perangkat Lunak\n' \
		'== TUGAS == \n' \
		'Tugas 1 : 88 \n' \
		'Tugas 2 : 88 \n' \
		'Tugas 3 : 88 \n' \
		'Tugas 4 : 87 \n' \
		'Tugas 5 : 88 \n' \
		'== UJIAN == \n' \
		'UTS : 54'))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Masih ada kesempatan untuk meraih nilai yang lebih tinggi di UAS nanti. Semangat!'))
	elif (event.message.text.lower() == "wbd"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Nilai tidak ditemukan untuk mata kuliah Web-based Development.'))
	elif (event.message.text.lower() == "mbd"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Manajemen Basis Data\n' \
		'== KUIS == \n' \
		'Kuis 1 : 45 \n' \
		'Kuis 2 : 60 \n' \
		'== TUGAS == \n' \
		'Tugas 1 : 95 \n' \
		'== UJIAN == \n' \
		'UTS : 67'))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Jangan biarkan soal beranak itu melunturkan semangatmu! Kamu masih memiliki kesempatan untuk memperbaiki nilaimu. Berjuanglah!'))
	elif (event.message.text.lower() == "to-do list"):
		# jika tombol to-do list ditekan
		# fungsi yang akan dilakukan ditulis dibawah ini
		toDoListMenu = ButtonsTemplate(
			title='To-do List Menu', text='Pilih salah satu', thumbnail_image_url='https://raw.githubusercontent.com/alvinlimassa/upi-bot/todolist/Image/todolist.png?token=AZu-_q7EbEcr2o4ChRGwXOrzCXqetxNcks5b7p25wA%3D%3D',actions=[
				MessageAction(label='Tampilkan Semua', text='Tampilkan Semua To-do List'),
				DatetimePickerTemplateAction(label='Pilih tanggal', data='datetime_postback', mode='date'),
				MessageAction(label='Tambah To-do List', text='Tambah To-do List')
			])
		toDoListMessage = TemplateSendMessage(alt_text='To do List Menu', template=toDoListMenu)
		line_bot_api.reply_message(event.reply_token, toDoListMessage)
	elif (event.message.text.lower() == "tampilkan semua to-do list"):
		# jika user meminta menampilkan semua to-do list
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Berikut ini adalah To-Do List anda : \n' \
		'Senin, 12 November 2018 : \n' \
		'- 07.00 - 09.00 = AI \n' \
		'- 09.00 - 11.00 = IMK \n' \
		'- PR IMK (Deadline 10.00)\n' \
		'Selasa, 13 November 2018 : \n' \
		'- 07.00 - 09.00 = WBD\n' \
		'- 09.00 - 11.00 = JARKOM'))
		line_bot_api.push_message(
			event.source.user_id,
			TextSendMessage(
				text='Tekan/ ketik Selanjutnya untuk menampilkan to-do list berikutnya',
				quick_reply=QuickReply(
					items=[
						QuickReplyButton(
							action=MessageAction(label='Selanjutnya', text='to-do list lanjut')
						),
					])))
	elif (event.message.text.lower() == "to-do list lanjut"):
		# jika user meminta menampilkan Lanjutan To-do list
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Berikut ini adalah To-Do List anda : \n' \
		'Rabu, 14 November 2018 : \n' \
		'- 07.00 - 08.00 = IMK \n' \
		'- 08.00 - 10.00 = AI \n' \
		'Kamis, 15 November 2018 : \n' \
		'- 07.00 - 09.00 = WBD\n' \
		'- 09.00 - 11.00 = JARKOM'))
	elif (event.message.text.lower() == "tambah to-do list"):
		# jika user ingin menambahkan jadwal
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Untuk menambahkan To-do List gunakan perintah = add: <judul to-do list>'))
	elif (event.message.text.lower() == "referensi"):
		# jika tombol referensi ditekan
		# fungsi yang akan dilakukan ditulis dibawah ini
		temp = [MessageAction(label=x.split(" ")[1], text=x.split(" ")[0] + " " + " ".join(x.split(" ")[2:])) for x in matkul_list]
		matkulMenu = CarouselTemplate(columns=[CarouselColumn(title=x.label, text=x.text, defaultAction=x, actions=[x]) for x in temp])
		matkulMessage = TemplateSendMessage(alt_text='Daftar mata kuliah', template=matkulMenu)
		line_bot_api.reply_message(event.reply_token, matkulMessage)
	elif (event.message.text.lower() == "if3110 pengembangan aplikasi berbasis web"):
		# referensi wbd
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Referensi IF3110 Pengembangan Aplikasi Berbasis Web\n\n' \
		'1. Web Technologies: A Computer Science Perspec4ve, Jeffrey C. Jackson, Pren4ce Hall, 2007\n\n' \
		'2. Developing Large Web Applica4ons: Producing Code That Can Grow and Thrive, Kyle Loudon, O\'Reilly Media, Inc., 2010\n\n' \
		'3. HTML5: Up and Running, Mark Pilgrim, O\'Reilly Media, Inc., 2010\n\n' \
		'4. The Java EE 6 Tutorial: Basic Concepts, Eric Jendrock & Ian Evans & Devika Gollapudi & Kim Haase & Chinmayee Srivathsa, Pren4ce Hall, 2010\n\n' \
		'5. JavaScript: The Defini4ve Guide, David Flanagan, O\'Reilly Media, 2011'))
	elif (event.message.text.lower() == "if3130 jaringan komputer"):
		# referensi jarkom
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Referensi IF3130 Jaringan Komputer\n\n' \
		'1. Computer Networks: A Systems Approach (4th Edition) by Larry Peterson and Bruce Davie. Morgan Kaufmann, 2007.\n\n' \
		'2. Lin, Y.-D. Computer Networks: An Open Source Approach McGraw Hills, 2011\n\n' \
		'3. Tanenbaum, Andrew, “Computer Networks”, 4th Ed. Prentice Hall, 2003\n\n' \
		'4. Stallings, William, “Data & Computer Communications”, Prentice Hall, 2002'))
	elif (event.message.text.lower() == "if3140 manajemen basis data"):
		# referensi mbd
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Referensi IF3140 Manajemen Basis Data\n\n' \
		'1. Silberschatz, H.F. Korth, S. Sudarshan, ‘Database System Concepts’, McGraw-Hill (Pustaka Utama)\n\n' \
		'2. J.A. Hoffer, M.B. Prescott, F.R. McFadden, ‘Modern Database Management’, Pearson Prentice Hall (Pendukung)\n\n' \
		'3. C.J. Date, ‘An Introduction to Database System’, Addison Wesley (Pendukung)'))
	elif (event.message.text.lower() == "if3150 manajemen proyek perangkat lunak"):
		# referensi mppl
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Referensi IF3150 Manajemen Proyek Perangkat Lunak\n\n' \
		'1. Information Technology Project Management 8th Edition, Kathy Schwalbe, Thomson Course Technology, 2015\n\n' \
		'2. A Guide to the Project Management Body of Knowledge, ANSI-PMI, 2008\n\n' \
		'3. Software Project, Steve McConnel, Microsoft Press, 1998\n\n' \
		'4. Project Management Professional Study Guide, Kim Heldman, Sybex, 2004\n\n' \
		'5. Wysocki, Robert K. Effective project management: traditional, agile, extreme. John Wiley & Sons, 2011'))
	elif (event.message.text.lower() == "if3151 interaksi manusia dan komputer"):
		# referensi wbd
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Referensi IF3151 Interaksi Manusia dan Komputer\n\n' \
		'1. Interaction Design - Beyond Human-Computer Interaction, Jenny Preece et al., John Wiley & Sons'))
	elif (event.message.text.lower() == "if3170 intelegensi buatan"):
		# referensi wbd
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Referensi IF3110 Pengembangan Aplikasi Berbasis Web\n\n' \
		'1. Stuart J Russell & Peter Norvig, Artificial Intelligence: A Modern Approach, 3rd Edition, Prentice-Hall International, Inc, 2010\n\n' \
		'2. Tom Mitchell, Machine Learning, 1999\n\n' \
		'3. MIT OpenCourseWare Website: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/'))
	elif (event.message.text.lower() == "presensi"):
		# jika tombol presensi ditekan
		# fungsi yang akan dilakukan ditulis dibawah ini
		presensiMenu = ButtonsTemplate(
			title='Pilih Jenis Presensi', text='Pilih salah satu', actions=[
				MessageAction(label='Semua Mata Kuliah', text='presensi-semua'),
				MessageAction(label='Spesific Mata Kuliah', text='presensi-spesific'),				
			])
		presensiMessage = TemplateSendMessage(alt_text='Presensi Menu', template=presensiMenu)
		line_bot_api.reply_message(event.reply_token, presensiMessage)
	
	elif(event.message.text.lower() == "presensi-semua"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('PRESENSI \n' \
		'============================\n' \
		'Jaringan Komputer : 20%\n'\
		'Manajemen Basis Data : 100%\n'\
		'Manajemen Proyek Perangkat Lunak : 80%\n'\
		'Interaksi Manusia Komputer : 100%\n'\
		'Web-Based Development : 80%\n'\
		'Intelegensi Buatan : 100%\n'\
		))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Semangat untuk jaringan komputernya, jangan menghilang seperti ninja :)'))
	elif (event.message.text.lower() == "presensi-spesific"):
		# jika tombol presensi ditekan
		# fungsi yang akan dilakukan ditulis dibawah ini
		menuSpesific = CarouselTemplate(
			columns=[
				CarouselColumn(
					title='IF3170', text='Inteligensi Buatan', defaultAction=MessageAction(label='Lihat presensi', text='presensi-IF3170'),
					actions=[MessageAction(label='Lihat presensi', text='presensi-IF3170')]
				),
				CarouselColumn(
					title='IF3130', text='Jaringan Komputer', defaultAction=MessageAction(label='Lihat presensi', text='presensi-IF3130'),
					actions=[MessageAction(label='Lihat presensi', text='presensi-IF3130')]
				),
				CarouselColumn(
					title='IF3151', text='Interaksi Manusia Komputer', defaultAction=MessageAction(label='Lihat presensi', text='presensi-IF3151'),
					actions=[MessageAction(label='Lihat presensi', text='presensi-IF3151')]
				),
				CarouselColumn(
					title='IF3150', text='Manajemen Proyek Perangkat Lunak', defaultAction=MessageAction(label='Lihat presensi', text='presensi-IF3150'),
					actions=[MessageAction(label='Lihat presensi', text='presensi-IF3150')]
				),
				CarouselColumn(
					title='IF3110', text='Web-Based Development', defaultAction=MessageAction(label='Lihat presensi', text='presensi-IF3110'),
					actions=[MessageAction(label='Lihat presensi', text='presensi-IF3110')]
				),
				CarouselColumn(
					title='IF3140', text='Manajemen Basis Data', defaultAction=MessageAction(label='Lihat presensi', text='presensi-IF3140'),
					actions=[MessageAction(label='Lihat presensi', text='presensi-IF3140')]
				)
			]
		)
		messageSpesific = TemplateSendMessage(alt_text='Tampilkan Nilai', template=menuSpesific)
		line_bot_api.reply_message(event.reply_token, messageSpesific)

	elif(event.message.text.lower() == "presensi-if3130"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('PRESENSI \n' \
		'============================\n' \
		'Jaringan Komputer : 20%\n'\
		'Jumlah Pertemuan : 20\n'\
		'Pertemuan tidak masuk : 3-18\n'\
		))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Semangat untuk kelas jarkomnya !!! '))

	elif(event.message.text.lower() == "presensi-if3140"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('PRESENSI \n' \
		'============================\n' \
		'Manajemen Basis Data : 100%\n'\
		'Jumlah Pertemuan : 20\n'\
		'Pertemuan tidak masuk : -\n'\
		))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Mantap sudah bagus !!!, Pertahankan !!!'))
	elif(event.message.text.lower() == "presensi-if3170"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('PRESENSI \n' \
		'============================\n' \
		'Intelegensi Buatan : 100%\n'\
		'Jumlah Pertemuan : 20\n'\
		'Pertemuan tidak masuk : -\n'\
		))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Mantap sudah bagus !!!, Pertahankan !!!'))
	elif(event.message.text.lower() == "presensi-if3150"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('PRESENSI \n' \
		'============================\n' \
		'Manajemen Proyek Perangkat Lunak : 80%\n'\
		'Jumlah Pertemuan : 20\n'\
		'Pertemuan tidak masuk : 19,20\n'\
		))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Absen masih aman, namun jatahmu sudah habis :( . Jangan bolos lagi !!!'))
	elif(event.message.text.lower() == "presensi-if3151"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('PRESENSI \n' \
		'============================\n' \
		'Interaksi Manusia Komputer : 100%\n'\
		'Jumlah Pertemuan : 20\n'\
		'Pertemuan tidak masuk : -\n'\
		))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Mantap sudah bagus !!!, Pertahankan !!!'))
	elif(event.message.text.lower() == "presensi-if3110"):
		line_bot_api.reply_message(event.reply_token, TextSendMessage('PRESENSI \n' \
		'============================\n' \
		'Web-Based Development : 80%\n'\
		'Jumlah Pertemuan : 20\n'\
		'Pertemuan tidak masuk : 19,20\n'\
		))
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Absen masih aman, namun jatahmu sudah habis :( . Jangan bolos lagi !!!'))
	elif (event.message.text.lower() == "aturan"):
		# jika tombol aturan ditekan
		# fungsi yang akan dilakukan ditulis dibawah ini
		aturanMenu = ButtonsTemplate(
			title='Prosedur dan Regulasi ITB', text='Pilih salah satu', actions=[
				MessageAction(label='Jadwal TU', text='Jadwal TU Kantor'),
				MessageAction(label='Pinjam Labtek V', text='Pinjam Labtek V'),
				MessageAction(label='KTM Hilang', text='KTM Hilang'),
				MessageAction(label='Transkrip', text='Permintaan Transkrip')
			])
		aturanMessage = TemplateSendMessage(alt_text='Menu aturan', template=aturanMenu)
		line_bot_api.reply_message(event.reply_token, aturanMessage)
	elif (event.message.text.lower() == "jadwal tu kantor"):
		# jadwal buka TU dan kantor
		line_bot_api.reply_message(event.reply_token, TextSendMessage('JADWAL BUKA TU DAN KANTOR \n' \
		'============================\n' \
		'\n' \
		'TU STEI \n' \
		'07.00 - 12.00  13.00 - 15.00 \n' \
		'LK ITB \n' \
		'07.00 - 12.00  13.00 - 16.30 \n' \
		'SP ITB\n' \
		'08.00 - 12.00  13.00 - 16.30'))
	elif (event.message.text.lower() == "pinjam labtek v"):
		# prosedur peminjaman ruangan labtek V
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Prosedur Peminjaman Ruangan Labtek V \n' \
		'================================ \n' \
		'\n' \
		'Prasyarat: \n' \
		'1. Biaya fotokopi Rp500,00 \n' \
		'\n' \
		'Prosedur: \n' \
		'1. Datang ke TU Lab Labtek V lantai 4 pada jam kerja\n' \
		'2. Isi surat peminjaman ruangan\n' \
		'3. Bawa surat peminjaman ke SP STEI Labtek VIII lantai 2 pada jam kerja\n'
		'4. Datang kembali ke SP STEI setelah 1 hari\n'
		'5. Ambil surat dan fotokopi 3 lembar\n'
		'6. Beri surat ke TU Lab dan dapur Labtek V lantai 4'))
	elif (event.message.text.lower() == "permintaan transkrip"):
		# prosedur permintaan transkrip
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Prosedur Permintaan Transkrip \n' \
		'========================= \n' \
		'\n' \
		'Prasyarat: \n' \
		'1. Biaya fotokopi Rp1.000,00 \n' \
		'2. Bolpoin\n' \
		'\n' \
		'Prosedur: \n' \
		'1. Datang ke TU STEI Labtek V lantai 2 pada jam kerja\n' \
		'2. Isi lembar permintaan surat\n' \
		'3. Kembalikan lembar ke TU\n' \
		'4. Datang kembali ke TU STEI setelah 3 hari\n' \
		'5. Ambil transkrip asli dan fotokopi 5 lembar\n' \
		'6. Bawa hasil fotokopi ke TU untuk dilegalisasi'))
	elif (event.message.text.lower() == "ktm hilang"):
		# prosedur permintaan KTM baru
		line_bot_api.reply_message(event.reply_token, TextSendMessage('Prosedur Penggantian KTM Hilang \n' \
		'============================ \n' \
		'\n' \
		'Prasyarat: \n' \
		'1. Surat keterangan hilang dari TU \n' \
		'2. Foto untuk KTM baru (digital)\n' \
		'3. Biaya penggantian Rp30.000,00\n' \
		'\n' \
		'Prosedur: \n' \
		'1. Datang ke Annex ITB dengan membawa prasyarat\n' \
		'2. Upload foto dan isi data di web sesuai dengan pemberitahuan\n' \
		'3. Ambil KTM baru di gedung CRCS pada waktu yang telah diberitahukan'))
	elif (event.message.text.lower() == "soal"):
		# jika tombol soal ditekan
		# fungsi yang akan dilakukan ditulis dibawah ini
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Pilih Mata Kuliah'))		
		menuQuiz = CarouselTemplate(
			columns=[
				CarouselColumn(
					title='AI', text='Inteligensi Buatan', defaultAction=MessageAction(label='Latihan', text='quiz-AI'),
					actions=[MessageAction(label='Latihan', text='quiz-AI')]
				),
				CarouselColumn(
					title='Jarkom', text='Jaringan Komputer', defaultAction=MessageAction(label='Latihan', text='quiz-Jarkom'),
					actions=[MessageAction(label='Latihan', text='quiz-Jarkom')]
				)
			]
		)
		messageQuiz = TemplateSendMessage(alt_text='Tampilkan Nilai', template=menuQuiz)
		line_bot_api.reply_message(event.reply_token, messageQuiz)
	elif (event.message.text.lower() == "quiz-ai"):
		menuQuiz = CarouselTemplate(
			columns=[
				CarouselColumn(
					title='Bab 1', text='Pengenalan AI', defaultAction=MessageAction(label='Mulai Quiz', text='quiz-pengenalan'),
					actions=[MessageAction(label='Mulai Quiz', text='quiz-pengenalan')]
				),
				CarouselColumn(
					title='Bab 2', text='Learning', defaultAction=MessageAction(label='Mulai Quiz', text='quiz-learning'),
					actions=[MessageAction(label='Mulai Quiz', text='quiz-learning')]
				)
			]
		)
		messageQuiz = TemplateSendMessage(alt_text='Tampilkan Nilai', template=menuQuiz)
		line_bot_api.reply_message(event.reply_token, messageQuiz)

	elif (event.message.text.lower() == "quiz-pengenalan"):
		# jika tombol aturan ditekan
		# fungsi yang akan dilakukan ditulis dibawah ini
		aturanMenu = ButtonsTemplate(
			title='Pengenalan', text='Mana yang bukan pendekatan AI?', actions=[
				MessageAction(label='Thinking Humanlly', text='TH'),
				MessageAction(label='Thinking Animally ', text='TA'),
				MessageAction(label='Acting Humanlly', text='AH'),
				MessageAction(label='Acting Rationally', text='AR')
			])
		aturanMessage = TemplateSendMessage(alt_text='To do List Menu', template=aturanMenu)
		line_bot_api.reply_message(event.reply_token, aturanMessage)
	elif (event.message.text.lower() == "th" or event.message.text.lower() == "ah" or event.message.text.lower() == "ar"):
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Persentase Kebenaran: 0%\n Ayo semangat ngerjainnya!'))
	elif (event.message.text.lower() == "ta"):
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Persentase Kebenaran: 100%\n Alhamdulillah bener semua'))
	else :
		inputTextA = event.message.text.lower().split(": ")
		inputTextB = event.message.text.lower().split(" :")
		inputTextC = event.message.text.lower().split(":")
		inputTextD = event.message.text.lower().split(" ")
		if (inputTextA[0] == "add" or inputTextA[0] == "referensi"):
    			inputText = inputTextA
		elif (inputTextB[0] == "add" or inputTextB[0] == "referensi"):
    			inputText = inputTextB
		elif (inputTextC[0] == "add" or inputTextC[0] == "referensi"):
    			inputText = inputTextC
		elif (inputTextD[0] == "add" or inputTextD[0] == "referensi"):
    			inputText = inputTextD
		else:
    			inputText = []
		if (inputText[0] == "add"):
			# fungsi untuk menambahkan to-do list
			global toDoListString
			toDoListString = 'Judul To-do List : ' + inputText[1]
			addToDoListMenu = ButtonsTemplate(
			title='Add To Do List', text=toDoListString , actions=[
				DatetimePickerTemplateAction(label='Pilih tanggal', data='todolist_datetime_postback', mode='datetime')
			])
			addToDoListMessage = TemplateSendMessage(alt_text='To do List Menu', template=addToDoListMenu)
			line_bot_api.reply_message(event.reply_token, addToDoListMessage)
		elif (inputText[0] == "referensi"):
			# fungsi untuk mencari referensi dengan keyword mata kuliah
			temp = [MessageAction(label=x.split(" ")[1], text=x.split(" ")[0] + " " + " ".join(x.split(" ")[2:])) for x in matkul_list if inputText[1].lower() in x.lower()]
			if(temp):
				matkulMenu = CarouselTemplate(columns=[CarouselColumn(title=x.label, text=x.text, defaultAction=x, actions=[x]) for x in temp])
				matkulMessage = TemplateSendMessage(alt_text='Daftar mata kuliah', template=matkulMenu)
				line_bot_api.reply_message(event.reply_token, matkulMessage)
			else:
				line_bot_api.reply_message(event.reply_token, TextSendMessage('Tidak ditemukan mata kuliah terkait ' + '\'' +inputText[1] + '\''))
		else :
			line_bot_api.reply_message(event.reply_token, TextSendMessage("Maaf, kami tidak mengerti permintaan anda harap cek kembali input anda"))
	

@handler.add(PostbackEvent)
def handle_postback(event):
	if event.postback.data == 'datetime_postback':
		selectedDate = datetime.datetime.strptime(event.postback.params['date'], '%Y-%m-%d')
		dateNewFormat = datetime.date.strftime(selectedDate, "%d %B %Y")
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text= 'To-do List pada ' + dateNewFormat + ':\n'\
		'- 07.00 - 09.00 = WBD\n'\
		'- 09.00 - 11.00 = AI'))
	elif event.postback.data == 'todolist_datetime_postback':
		global toDoListString
		dateAndTime = event.postback.params['datetime'].split("T")
		selectedDate = datetime.datetime.strptime(dateAndTime[0], '%Y-%m-%d')
		dateNewFormat = datetime.date.strftime(selectedDate, "%d %B %Y")
		toDoListString += '\ntanggal: ' + dateNewFormat + '\nPukul : ' + dateAndTime[1] + '\nberhasil ditambahkan'
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text=toDoListString))
		confirm_template = ConfirmTemplate(text='Apakah ingin mengaktifkan reminder untuk to-do list yang baru ditambahkan?', actions=[
			PostbackAction(label='Yes', data='reminderON'),
			PostbackAction(label='No', data='reminderOFF'),
		])
		template_message = TemplateSendMessage(
			alt_text='Confirm alt text', template=confirm_template)
		line_bot_api.reply_message(event.reply_token, template_message)
	elif event.postback.data == 'reminderON':
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text="Reminder berihasil diaktifkan"))
	elif event.postback.data == 'reminderOFF':
		line_bot_api.push_message(event.source.user_id, TextSendMessage(text="Reminder tidak diaktifkan"))
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
