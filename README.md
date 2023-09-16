# Hava Durumu Uygulaması

Bu basit hava durumu uygulaması, belirli bir şehir için OpenWeatherMap API'sini kullanarak güncel hava koşullarını kontrol etmenizi sağlar. Şehir adını girerek, uygulama sıcaklık, açıklama, nem ve daha fazlası dahil olmak üzere hava bilgilerini görüntüler.

## Özellikler

- OpenWeatherMap API'sinden gerçek zamanlı hava verilerini çeker.
- Hava açıklaması, sıcaklık, en düşük ve en yüksek sıcaklık, nem ve hissedilen sıcaklığı görüntüler.
- Farklı şehirler için hava bilgisi arama desteği sağlar.

## Başlarken

Bu hava durumu uygulamasını kullanmak için OpenWeatherMap'den bir API anahtarı almanız gerekmektedir. Başlamak için aşağıdaki adımları izleyin:

1. OpenWeatherMap hesabı oluşturun, eğer yoksa.
2. OpenWeatherMap web sitesinden bir API anahtarı oluşturun.
3. Kod içindeki `YOUR_API_KEY` ifadesini kendi API anahtarınızla değiştirin.(Not: kodun içinde kendi API anahtarım vardır 
isterseniz kendi API anahtarınız ile değiştirebilirsiniz)

## Kullanım

1. Bu depoyu yerel makinenize `git clone` komutu ile klonlayın.
2. Gerekli Python kütüphanelerini `pip install requests Pillow` komutu ile kurun.
3. `hava durumu.py` betiğini Python ile çalıştırın.

```shell
python hava durumu.py

1.Şehir adı sorulduğunda istediğiniz şehri girin.
2.Hava bilgilerini konsolda görüntüleyin.
3.Uygulamadan çıkmak için şehir adı sorulduğunda 'quit' veya 'q' yazın.

## Teşekkürler
Hava verileri OpenWeatherMap tarafından sağlanmaktadır.

Bu README dosyasını projeniz hakkında daha fazla bilgi, ek özellikler, kullanım talimatları, ekran görüntüleri ve teşekkürler dahil olmak üzere özelleştirmekte özgürsünüz. Hava durumu uygulamanızı geliştirdikçe ve iyileştirdikçe README dosyasını güncel tutmayı unutmayın.
