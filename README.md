## �{��{���һݳn��H�Ϊ���
###### (�i�����p����s�A�������u���@�w�i���椧����)
### �һݳn��:
|�n��W��|�n�骩��|
|---     |---     |
|python|3.6.5|
|Django|2.0.2|
|django-allauth|0.35.0|
|pydub|0.23.0|
|ffmpeg|
|tensorflow|1.9.0|
###### �Բӥi�H�Ѧ�environment.txt

## �ϥε{��
### �������:
�T�{���|������Ƨ��A�}��cmd��J:
```
python manage.py runserver
```
�Y�i�ϥ�
### �W���ɮ�:
�b�������I��W�ǩΥ����W�ǡA�����ɮ׷|�x�s��document���

## ��z�ɮפ�python�{��

#### 1. readAudio.py :
���{���i�H��z��Ƨ���������data�ƾڡA�C�Ӥ奻���O���ֿ��F�h�֭Өÿ�X��CSV�ɡC�i�b�����ק�mypath�ӫ��w���i��έp����Ƨ��C�`:���{���|Ū��conv_labels.txt�ӿ�ܤl��Ƨ�����
#### 2. testAcc.py:
���{���i�H�Ψӿz�墨���ɮ׬����Ϊ�training���ɮסC���ɮ׷|�hŪmy_frozen_graph.pb�i����ѿz��A�ñN�̫᪺���ѵ��G���ƤJ�e�T�W�̡A��X��@�ӦW��WavOK����Ƨ��C�`:���{���|Ū��conv_labels.txt�ӿ�ܤl��Ƨ�����
#### 3. transTo16K.py:
�i�H�Nwav�ɥ����ഫ���A�itraning��16K�ɮסC�i�b�����ק�mypath�ӫ��w���i���ഫ����Ƨ�