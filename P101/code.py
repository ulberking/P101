access = 'sl.BDbbSo6fssnmLZhADNR13qRnM8sMkMrHHBi9314-2pXoOGOuRxEXDbpy6awZpjaW2-v_pdNUtbIZ3DBv0p3R3nZ3AVmG4cu4ydU7LDHf7ovTexXvhO871JXS3x925E8jxY5GORCsisc'
import dropbox
dbx=dropbox.Dropbox(access)
f=open('harry.png','rb')
dbx.files_upload(f.read(),'/Minho/harry.png')