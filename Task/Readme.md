## FLEXBOX FROGGY - bütün tapşırıqlar  bitdi.

 <!-- .............................................................................................. -->


# Translator ve assembler nədir? Compiler və interpreter ilə aralarındakı fərqlər nələrdir?

Translator- “machine code”-dan fərqli dillərdə yazılan kodu(source code) “machine code”-a(object code) çevirmək üçün istifadə olunur. Bu translator-un müxtəlif növləri vardır.

- Assembler
- İnterpreter
- Compiler

### Assembler: Assembly dili maşın dilindən irəli gələn çətinlikləri aradan qaldırmaq üçün hazırlanmış bir proqramlaşdırma dilidir.  Assembly  dilində ikili sistemdən istifadə edərək bir proqram yazmaq əvəzinə, qısa sözlərdən əmrlər (mnemonics) istifadə olunur.

Assembler- assembly language-də yazılan kodları(source code) bir-bir analiz edərək onları machine code-a(object code) tərcümə edən proqrama deyilir.
Hər bir CPU şirkəti, spesifik maşın dilinə görə assembly dili və assembler proqramına malikdir.
 Assembler əvvəlcə bütün proqramı bir-başa tərcümə edir və yalnız ondan sonra proqramı “run” edir.
- Error-lar proqram “run” edilmədən öncə göstərilir.
- Sadəcə bir dəfə proqram tərcümə edilir, yenidən işlədildiyi zaman təkrar tərcümə etməyə ehtiyac qalmır.
- Az yaddaşa ehtiyac duyulur.

### Compiler: Hər hansı bir proqramlaşdırma dilindən istifadə edərək inkişaf etmiş daha üst səviyyəli proqramlaşdırma dili tərəfindən yazılmış mənbə kodunu kompüterin anlaya biləcəyi maşın dilinə, yəni 0 və 1-lərə çevirən vasitəçi proqramdır. Burda yazdığımız kodları bütünlüklə “machine code”-a çevirir. 
Əgər kodda sintaktik və ya semantik hər hansı bir səhvlik varsa, compiler əvvəlcə bütün programı yoxlayacaq sonra isə həmin səhvlikləri göstərəcək. Bütün bu problemləri düzəltmədən proqramın işləməsi mümkün deyil.Compiler istifadə edən dillərə misal olaraq, C, C++ dillərini göstərə bilərik.

### İnterpreter:  yüksək səviyyəli proqramlaşdırma dilində yazılmış bir proqramı addım-addım maşın dilinə çevirən və maşın dilində təlimatları icra edən bir proqramdır.Compiler-dan fərqli olaraq interpreter bir sətir kodu oxuyur və dərhal icra edir.

 ## Compiler və interpreter ilə aralarındakı fərqlər nələrdir?
 
 * Compiler kodları icra etmədən öncə bütün proqramı “machine code”-a çevirir.
 * Interpreter programı sətirbəsətir “machine code”-a çevirir və kodları ardıcıllıqla icra edir.
 * Compiler- kodlar daha sürətli icra olunur.
 * İnterpreter - Kodlar daha yavaş ra olunur.
 * Compiler- daha çox yaddaş tələb olunur.
 * İnterpreter- daha az yaddaş tələb olunur çünki saxlayacq bir aralıq kod yaratmır.
 * Compiler- Bütün kodlar artıq tərcümə olunduğu üçün, növbəti dəfə proqramı icra edəndə çox daha az vaxt tələb olunur.
 * İnterpreter-bir-bir icra etdiyi üçün daha çox vaxt tələb olunur.
 * Compiler- Bütün xətaları aşkarlayıb proqramı tam tərcümə edəndən sonra göstərir.
 * İnterpreter- İlk xətada proqram tərcümə etməyi saxlayır,koddakı hər bir səhvi bir-bir göstərir.
 
 <!-- .............................................................................................. -->

## - Javascript operatorlar haqqinda umumi melumatlari oxudum.
## - JavaScript DataTypes haqqinda umumi melumatlari oxudum.

# JavaScript Function:
Javascript ile yazilmis bir funksiya müəyyən bir əməliyyatı yerinə yetirmək üçün hazırlanmış bir kod blokudur.
Bir məqsədə xidmət edən proqram parçalarıdır.Funksiya icra edildikdə, bir əməliyyat yerinə yetirməsi və ya bir dəyəri qaytarması teleb olunur.

 ##  - Prompt metodu ve Javascript Function istifade edib toplama emeliyyatini yazdim


# Günümüzdə istifadə olunan Js,PHP,Python və C# dillərində ortaq istifadə olunan data növləri hansılardır və qısaca izahatlarını yazın.
   - Ortaq Data types:
        * string : mətn dəyərlərini proqramdakı bir string dəyişkəndə saxlayırıq.
        * Number : 
             - tam ədədi saxlaya bilir və məlumat aralığı genişdirş
             - İnt tipli dəyişənlər 32 bit-lik deyeri saxlayır.
             - float onluq ədədlərdən ibarət dəyişən tipi
        * Boolean -"Doğru" və "Yanlış" olaraq iki dəyər alan bir dəyişkən növüdür.
          İdarəetmə proseslərində tez-tez istifadə olunur.


#JS metodları
-document.getElementById(id)
* müəyyən edilmiş dəyər ilə ID atributu olan elementi qaytarır.
* return metoddur
* object tipində məlumat qaytarır
* string tipində argument tələb edir
-document.getElementsByTagName(name)
* GetElementsByTagName () bir HTMLCollection qaytarır.GetElementsByTagName (tagname) metodu sənəddəki (sənəd üçün) və ya NodeList obyekti (qovşaqların toplusu) olaraq göstərilən etiketi olan uşaq qovşaqları (qovşaq üçün) arasında tapılmış bütün elementləri qaytarır. 
* return metoddur
* object tipində məlumat qaytarır
* string tipində argument tələb edir
-document.getElementsByClassName(name)
* bu metod bu metodun parametrində göstərilən sinif adına malik elementlər (qovşaqlar) toplusu olan NodeList obyektini qaytarır.
* return metoddur
* object tipində məlumat qaytarır
* parametrinde string tipli argument tələb edir
- document.querySelector()
* QuerySelector () metodu sənəddə (sənəd üçün) və ya bu metodun parametri olaraq göstərilən CSS seçicisinə uyğun uşaq qovşaqları arasında (qovşaq üçün) tapılan ilk elementi qaytarır. CSS seçicisinə heç bir element uyğun gəlmirsə, bu metod null qaytarır.
* return metoddur
* object tipində məlumat qaytarır
* parametrinde string tipli argument tələb edir.
