FLEXBOX FROGGY - bütün tapşırıqlar  bitdi.

...............................................

Translator ve assembler nədir? Compiler və interpreter ilə aralarındakı fərqlər nələrdir?

Translator- “machine code”-dan fərqli dillərdə yazılan kodu(source code) “machine code”-a(object code) çevirmək üçün istifadə olunur. Bu translator-un müxtəlif növləri vardır.

- Assembler
- İnterpreter
- Compiler

Assembler- Assembly dili maşın dilindən irəli gələn çətinlikləri aradan qaldırmaq üçün hazırlanmış bir proqramlaşdırma dilidir.  Assembly  dilində ikili sistemdən istifadə edərək bir proqram yazmaq əvəzinə, qısa sözlərdən əmrlər (mnemonics) istifadə olunur.
Assembler- assembly language-də yazılan kodları(source code) bir-bir analiz edərək onları machine code-a(object code) tərcümə edən proqrama deyilir.
Hər bir CPU şirkəti, spesifik maşın dilinə görə assembly dili və assembler proqramına malikdir.
 Assembler əvvəlcə bütün proqramı bir-başa tərcümə edir və yalnız ondan sonra proqramı “run” edir.
— Error-lar proqram “run” edilmədən öncə göstərilir.
— Sadəcə bir dəfə proqram tərcümə edilir, yenidən işlədildiyi zaman təkrar tərcümə etməyə ehtiyac qalmır.
— Az yaddaşa ehtiyac duyulur.

Compiler- Hər hansı bir proqramlaşdırma dilindən istifadə edərək inkişaf etmiş daha üst səviyyəli proqramlaşdırma dili tərəfindən yazılmış mənbə kodunu kompüterin anlaya biləcəyi maşın dilinə, yəni 0 və 1-lərə çevirən vasitəçi proqramdır. Burda yazdığımız kodları bütünlüklə “machine code”-a çevirir. 
Əgər kodda sintaktik və ya semantik hər hansı bir səhvlik varsa, compiler əvvəlcə bütün programı yoxlayacaq sonra isə həmin səhvlikləri göstərəcək. Bütün bu problemləri düzəltmədən proqramın işləməsi mümkün deyil.Compiler istifadə edən dillərə misal olaraq, C, C++ dillərini göstərə bilərik.

İnterpreter-  yüksək səviyyəli proqramlaşdırma dilində yazılmış bir proqramı addım-addım maşın dilinə çevirən və maşın dilində təlimatları icra edən bir proqramdır.Compiler-dan fərqli olaraq interpreter bir sətir kodu oxuyur və dərhal icra edir.

 Compiler və interpreter ilə aralarındakı fərqlər nələrdir?
 
 Compiler kodları icra etmədən öncə bütün proqramı “machine code”-a çevirir.
 Interpreter programı sətirbəsətir “machine code”-a çevirir və kodları ardıcıllıqla icra edir.
 Compiler- kodlar daha sürətli icra olunur.
 İnterpreter - Kodlar daha yavaş ra olunur.
 Compiler- daha çox yaddaş tələb olunur.
 İnterpreter- daha az yaddaş tələb olunur çünki saxlayacq bir aralıq kod yaratmır.
 Compiler- Bütün kodlar artıq tərcümə olunduğu üçün, növbəti dəfə proqramı icra edəndə çox daha az vaxt tələb olunur.
 İnterpreter-bir-bir icra etdiyi üçün daha çox vaxt tələb olunur.
 Compiler- Bütün xətaları aşkarlayıb proqramı tam tərcümə edəndən sonra göstərir.
 İnterpreter- İlk xətada proqram tərcümə etməyi saxlayır,koddakı hər bir səhvi bir-bir göstərir.
 
 
