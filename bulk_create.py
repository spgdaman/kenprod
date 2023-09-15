from django.contrib.auth.hashers import make_password
from accounts.models import User

# User = models.User

# User.objects.bulk_create([
#     User(
#         username=name,
#         email='sample@email.co.uk',
#         password=make_password('Sample&Password!'),
#         is_active=True,
#     )
# ])

user_list = [
    User(first_name='Justine',last_name='',mobile_number='0733444025',username='justine',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Milkah',last_name='Muthoni',mobile_number='0726435956',username='milkah_muthoni',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Vincent',last_name='Odhe',mobile_number='0780427558',username='vincent_odhe',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Jesca',last_name='Emily',mobile_number='0711640285',username='jesca_emily',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Eric',last_name='Msa',mobile_number='0733444022',username='eric_msa',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Teresa',last_name='Wamuchii',mobile_number='011321348',username='teresa_wamuchii',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Mushtak',last_name='Hussein',mobile_number='0738577707',username='mushtak_hussein',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Himashu',last_name='Khetia',mobile_number='0734723723',username='himashu_khetia',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Brian',last_name='Owiti',mobile_number='0705606468',username='brian_owiti',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Grace',last_name='Wambui',mobile_number='0710735242',username='grace_wambui',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Sharon',last_name='Jepkoech',mobile_number='0706802500',username='sharon_jepkoech',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Daniel',last_name='Amukowa',mobile_number='0798689971',username='daniel_amukowa',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Bates',last_name='Luseka',mobile_number='0725780680',username='bates_luseka',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='John',last_name='Muhoti',mobile_number='0733444021',username='john_muhoti',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Nelly',last_name='Kebaso',mobile_number='0797582425',username='nelly_kebaso',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='John',last_name='Kombo',mobile_number='0727976502',username='john_kombo',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Laban',last_name='Mgaza',mobile_number='0743672203',username='laban_mgaza',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Rosemary',last_name='Njoki',mobile_number='0792433006',username='rosemary_njoki',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Loise',last_name='Wanjiru',mobile_number='0727085106',username='loise_wanjiru',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Angima',last_name='Beatrice',mobile_number='0724943656',username='angima_beatrice',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Stanislous',last_name='Masila',mobile_number='0733444029',username='stanislous_masila',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Tumaini',last_name='Were',mobile_number='0759581179',username='tumaini_were',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Lucia',last_name='Ayako',mobile_number='0741456998',username='lucia_ayako',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Gloriah',last_name='Wiabule',mobile_number='0727747863',username='gloriah_wiabule',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Joyce',last_name='Njeri',mobile_number='0752901785',username='joyce_njeri',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),
User(first_name='Ezekiel',last_name='Opati',mobile_number='0733595604',username='ezekiel_opati',is_active='True',is_staff='True',is_admin='False',password=make_password('Kenp*1234'),),

]

User.objects.bulk_create(user_list)