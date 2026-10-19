Pertama Install driver :

1. Hubungkan RTL.SDR di port usb laptop/pc 

2. Open zadig.exe

3. Klik Options -> Klik List All Devices -> Bulk-In,Interface(Interface 0) -> Install Driver WinUSB

Kedua Install Virtual Radar : 

1. Open VirtualRadarSetup.exe di dalam folder dump1090-rtl-sdr

Ketiga Jalankan Aplikasi (Online/Offline) : 

	* Online :
		
		1.  Open adsb(online).bat
	
	* Offline :

		1. Install TileServerCachePluginSetup.exe di mana saja
	
		2. Open folder hasil Install TileServerCachePluginSetup.exe

		3. Copy semua isinya dan paste di folder hasil install VirtualRadarSetup.exe

		4. Open VirtualRadar.exe 

		5. Klik Tools -> Plugins -> Options -> Centang Plugin Enabled -> Klik OK -> Klik Close

		6. Jalankan http://127.0.0.1/VirtualRadar

		7. Zoom in daerah-daerah yang ingin di download(Membutuhkan Koneksi Internet Untuk Download Map)

		8. Setelah selesai tutup map dan buka kembali VirtualRadar.exe

		9. Klik Tools -> Download Data -> Download -> Close

		10. Klik Tools -> Plugins -> Options -> Centang Offline mode enabled -> Klik OK -> Klik Close

		11. Tutup aplikasi VirtualRadar.exe

		12. Jalankan Open adsb(offline).bat 







