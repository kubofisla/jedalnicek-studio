from sqlalchemy.orm import Session
from database.schema import Meal, Ingredient, MealIngredientMap, Plan, PlanGroup, Tag, MealTagMap, User

def insertDefaultData(engine):
    with Session(engine) as session:
        ingredients = {
            "ryze_jasminova" : Ingredient(sName="Rýže jasmínová", nEnergy=348.57, nProtein=8.00, nFat=0.00, nCarbohydrate=79.00, nSugar=0.00, nDietaryFiber=1.00),
            "jablko" : Ingredient(sName="Jablko", nEnergy=56.69, nProtein=0.00, nFat=0.00, nCarbohydrate=13.07, nSugar=11.07, nDietaryFiber=3.07),
            "banany" : Ingredient(sName="Banány", nEnergy=81.28, nProtein=1.17, nFat=0.25, nCarbohydrate=21.83, nSugar=14.92, nDietaryFiber=2.08),
            "vejce_slepici_m" : Ingredient(sName="Vejce slepičí M 55g/ks", nEnergy=151.13, nProtein=12.36, nFat=10.91, nCarbohydrate=0.91, nSugar=0.00, nDietaryFiber=0.00),
            "mandle" : Ingredient(sName="Mandle", nEnergy=591.30, nProtein=20.50, nFat=53.50, nCarbohydrate=18.50, nSugar=4.00, nDietaryFiber=12.00),
            "boruvky" : Ingredient(sName="Borůvky", nEnergy=54.07, nProtein=1.00, nFat=0.00, nCarbohydrate=11.00, nSugar=6.00, nDietaryFiber=5.00),
            "kefirove_mleko_bile_1,5%_kunin" : Ingredient(sName="Kefírové mléko bílé 1,5% Kunín", nEnergy=40.91, nProtein=3.30, nFat=1.50, nCarbohydrate=3.50, nSugar=3.30, nDietaryFiber=0.00),
            "orechy_vlasske" : Ingredient(sName="Ořechy vlašské", nEnergy=669.50, nProtein=16.00, nFat=63.00, nCarbohydrate=14.00, nSugar=3.00, nDietaryFiber=6.00),
            "slunecnicova_seminka" : Ingredient(sName="Slunečnicová semínka", nEnergy=591.90, nProtein=19.00, nFat=45.00, nCarbohydrate=28.00, nSugar=5.00, nDietaryFiber=11.00),
            "kvaskovy_chleb" : Ingredient(sName="Kváskový chléb", nEnergy=230.00, nProtein=9.00, nFat=1.83, nCarbohydrate=50.17, nSugar=0.83, nDietaryFiber=7.00),
            "jihocesky_tvaroh_polotucny_madeta" : Ingredient(sName="Jihočeský tvaroh polotučný Madeta", nEnergy=95.10, nProtein=10.24, nFat=4.40, nCarbohydrate=3.60, nSugar=3.60, nDietaryFiber=0.00),
            "maslo_80_%_president" : Ingredient(sName="Máslo 80 % Président", nEnergy=712.90, nProtein=0.00, nFat=80.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "zakysana_smetana_15_%_kunin" : Ingredient(sName="Zakysaná smetana 15 % Kunín", nEnergy=160.28, nProtein=2.20, nFat=15.00, nCarbohydrate=3.40, nSugar=3.40, nDietaryFiber=0.00),
            "cibule" : Ingredient(sName="Cibule", nEnergy=40.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "paprika_cervena" : Ingredient(sName="Paprika červená", nEnergy=35.17, nProtein=1.00, nFat=0.00, nCarbohydrate=6.00, nSugar=4.00, nDietaryFiber=4.00),
            "paprika_sladka" : Ingredient(sName="Paprika sladká", nEnergy=359.33, nProtein=13.33, nFat=13.33, nCarbohydrate=33.33, nSugar=0.00, nDietaryFiber=0.00),
            "chia_seminka" : Ingredient(sName="Chia semínka", nEnergy=525.10, nProtein=11.00, nFat=31.00, nCarbohydrate=25.00, nSugar=1.00, nDietaryFiber=0.00),
            "mrazene_boruvky" : Ingredient(sName="Mražené borůvky", nEnergy=70.10, nProtein=0.60, nFat=0.60, nCarbohydrate=15.80, nSugar=15.00, nDietaryFiber=7.00),
            "mandlove_mleko_dm_bio" : Ingredient(sName="Mandlové mléko DM Bio", nEnergy=45.94, nProtein=1.40, nFat=3.60, nCarbohydrate=2.20, nSugar=2.20, nDietaryFiber=0.00),
            "bio_kakao_horke" : Ingredient(sName="BIO kakao hořké", nEnergy=337.00, nProtein=28.00, nFat=12.00, nCarbohydrate=14.00, nSugar=0.00, nDietaryFiber=34.00),
            "horka_cokolada_lindt_85%" : Ingredient(sName="Hořká čokoláda Lindt 85%", nEnergy=577.30, nProtein=13.00, nFat=46.00, nCarbohydrate=19.00, nSugar=11.00, nDietaryFiber=0.00),
            "jahly" : Ingredient(sName="Jáhly", nEnergy=361.49, nProtein=11.14, nFat=4.00, nCarbohydrate=73.14, nSugar=0.00, nDietaryFiber=4.00),
            "mandarinky_ve_sladkem_nalevu_giana" : Ingredient(sName="Mandarinky ve sladkém nálevu Giana", nEnergy=64.35, nProtein=0.00, nFat=0.00, nCarbohydrate=15.00, nSugar=13.00, nDietaryFiber=0.00),
            "ovesne_vlocky" : Ingredient(sName="Ovesné vločky", nEnergy=364.80, nProtein=13.00, nFat=9.00, nCarbohydrate=47.00, nSugar=1.00, nDietaryFiber=18.00),
            "mleko_plnotucne_3,5%" : Ingredient(sName="Mléko plnotučné 3,5%", nEnergy=63.61, nProtein=3.20, nFat=3.50, nCarbohydrate=4.80, nSugar=0.00,
            nDietaryFiber=0.00),
            "recky_jogurt_milko_5%" : Ingredient(sName="Řecký jogurt Milko 5%", nEnergy=94.74, nProtein=8.00, nFat=5.00, nCarbohydrate=4.00, nSugar=4.00, nDietaryFiber=0.00),
            "maliny" : Ingredient(sName="Maliny", nEnergy=34.39, nProtein=1.20, nFat=0.60, nCarbohydrate=12.80, nSugar=3.00, nDietaryFiber=6.40),
            "hummus_original_yami" : Ingredient(sName="Hummus original Yami", nEnergy=190.19, nProtein=5.29, nFat=12.00, nCarbohydrate=14.00, nSugar=0.57, nDietaryFiber=0.00),
            "dusena_sunka_veprova_96%_dulano" : Ingredient(sName="Dušená šunka vepřová 96% Dulano", nEnergy=104.07, nProtein=20.00, nFat=2.00, nCarbohydrate=1.00, nSugar=1.00, nDietaryFiber=0.00),
            "eidam_30_%_blanik" : Ingredient(sName="Eidam 30 % Blaník", nEnergy=264.35, nProtein=29.00, nFat=16.00, nCarbohydrate=0.50, nSugar=0.50, nDietaryFiber=0.00),
            "mrkev" : Ingredient(sName="Mrkev", nEnergy=35.41, nProtein=1.00, nFat=0.00, nCarbohydrate=7.00, nSugar=6.00, nDietaryFiber=4.00),
            "moravske_okurky_efko" : Ingredient(sName="Moravské okurky Efko", nEnergy=33.74, nProtein=0.60, nFat=0.00, nCarbohydrate=7.80, nSugar=6.00,
            nDietaryFiber=0.00),
            "hermelin_kral_syru" : Ingredient(sName="Hermelín Král Sýrů", nEnergy=329.18, nProtein=18.00, nFat=28.00, nCarbohydrate=2.00, nSugar=0.60, nDietaryFiber=0.00),
            "recky_jogurt_0%_tuku_milko" : Ingredient(sName="Řecký jogurt 0% tuku Milko", nEnergy=57.41, nProtein=10.00, nFat=0.00, nCarbohydrate=4.00,
            nSugar=3.00, nDietaryFiber=0.00),
            "testoviny_panzani" : Ingredient(sName="Těstoviny Panzani", nEnergy=366.27, nProtein=12.00, nFat=2.00, nCarbohydrate=72.00, nSugar=3.67, nDietaryFiber=3.67),
            "susena_rajcata_franz_josef" : Ingredient(sName="Sušená rajčata Franz Josef", nEnergy=247.60, nProtein=7.25, nFat=13.00, nCarbohydrate=26.00, nSugar=8.25, nDietaryFiber=0.00),
            "mozzarella_light_galbani" : Ingredient(sName="Mozzarella light Galbani", nEnergy=172.73, nProtein=18.00, nFat=11.00, nCarbohydrate=1.58, nSugar=0.92, nDietaryFiber=0.00),
            "polnicek" : Ingredient(sName="Polníček", nEnergy=13.16, nProtein=1.40, nFat=0.20, nCarbohydrate=2.20, nSugar=1.00, nDietaryFiber=1.20),
            "okurky" : Ingredient(sName="Okurky", nEnergy=10.25, nProtein=0.80, nFat=0.20, nCarbohydrate=2.30, nSugar=0.70, nDietaryFiber=0.90),
            "olej_olivovy" : Ingredient(sName="Olej olivový", nEnergy=885.20, nProtein=0.00, nFat=100.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "basmati_ryze_vitana" : Ingredient(sName="Basmati rýže Vitana", nEnergy=355.27, nProtein=8.67, nFat=0.33, nCarbohydrate=77.00, nSugar=0.00,
            nDietaryFiber=1.33),
            "losos_obecny" : Ingredient(sName="Losos obecný", nEnergy=174.15, nProtein=20.00, nFat=10.42, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "avokado" : Ingredient(sName="Avokádo", nEnergy=243.54, nProtein=2.00, nFat=24.00, nCarbohydrate=6.00, nSugar=0.00, nDietaryFiber=5.00),
            "kukurice_bonduelle" : Ingredient(sName="Kukuřice Bonduelle", nEnergy=79.90, nProtein=3.00, nFat=2.00, nCarbohydrate=11.00, nSugar=5.00, nDietaryFiber=4.00),
            "sojova_omacka" : Ingredient(sName="Sójová omáčka", nEnergy=57.70, nProtein=8.00, nFat=0.00, nCarbohydrate=7.00, nSugar=0.00, nDietaryFiber=0.00),
            "hovezi_maso_mlete" : Ingredient(sName="Hovězí maso mleté", nEnergy=224.97, nProtein=19.71, nFat=16.14, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "cuketa" : Ingredient(sName="Cuketa", nEnergy=20.34, nProtein=1.00, nFat=0.00, nCarbohydrate=3.00, nSugar=2.00, nDietaryFiber=1.00),
            "spaldova_mouka_celozrnna" : Ingredient(sName="Špaldová mouka celozrnná", nEnergy=345.94, nProtein=14.00, nFat=3.00, nCarbohydrate=70.00, nSugar=1.00, nDietaryFiber=9.00),
            "tunak_rio_mare_ve_vlastni_stave" : Ingredient(sName="Tuňák Rio Mare ve vlastní šťávě", nEnergy=0.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "olej_repkovy_aro" : Ingredient(sName="Olej řepkový ARO", nEnergy=814.40, nProtein=0.00, nFat=92.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "cesnek" : Ingredient(sName="Česnek", nEnergy=126.10, nProtein=6.00, nFat=0.00, nCarbohydrate=25.00, nSugar=3.00, nDietaryFiber=2.00),
            "ryzove_nudle" : Ingredient(sName="Rýžové nudle", nEnergy=364.36, nProtein=7.00, nFat=0.00, nCarbohydrate=86.00, nSugar=0.00, nDietaryFiber=7.00),
            "tofu_natural" : Ingredient(sName="Tofu natural", nEnergy=132.77, nProtein=15.00, nFat=7.00, nCarbohydrate=3.00, nSugar=2.00, nDietaryFiber=0.00),
            "med" : Ingredient(sName="Med", nEnergy=327.80, nProtein=0.00, nFat=0.00, nCarbohydrate=82.00, nSugar=82.00, nDietaryFiber=0.00),
            "citrony" : Ingredient(sName="Citróny", nEnergy=44.30, nProtein=1.00, nFat=0.00, nCarbohydrate=9.00, nSugar=3.00, nDietaryFiber=4.00),
            "cibule_cervena" : Ingredient(sName="Cibule červená", nEnergy=45.70, nProtein=1.33, nFat=0.33, nCarbohydrate=9.00, nSugar=6.00, nDietaryFiber=2.67),
            "rajcata_cherry" : Ingredient(sName="Rajčata Cherry", nEnergy=21.50, nProtein=0.88, nFat=0.24, nCarbohydrate=3.60, nSugar=2.64, nDietaryFiber=1.20),
            "makarony,_spagety" : Ingredient(sName="Makaróny, špagety", nEnergy=356.23, nProtein=12.67, nFat=1.33, nCarbohydrate=75.00, nSugar=0.00, nDietaryFiber=3.00),
            "free_form_bolonska_omacka_tesco" : Ingredient(sName="Free Form boloňská omáčka Tesco", nEnergy=42.11, nProtein=1.53, nFat=0.73, nCarbohydrate=6.60, nSugar=5.33, nDietaryFiber=1.53),
            "parmezan" : Ingredient(sName="Parmezán", nEnergy=389.90, nProtein=35.00, nFat=26.50, nCarbohydrate=3.00, nSugar=0.00, nDietaryFiber=0.00),
            "tortilla_wraps_(crusticroc)" : Ingredient(sName="Tortilla wraps (CrustiCroc)", nEnergy=310.28, nProtein=9.17, nFat=6.67, nCarbohydrate=51.00, nSugar=3.17, nDietaryFiber=0.00),
            "salat_ledovy" : Ingredient(sName="Salát ledový", nEnergy=16.02, nProtein=0.80, nFat=0.40, nCarbohydrate=2.00, nSugar=1.80, nDietaryFiber=1.40),
            "bio_recky_jogurt_bily_milko_5_%" : Ingredient(sName="BIO Řecký jogurt bílý Milko 5 %", nEnergy=94.74, nProtein=8.43, nFat=5.00, nCarbohydrate=4.00, nSugar=4.00, nDietaryFiber=0.00),
            "tortilla_wraps_celozrnna_lidl" : Ingredient(sName="Tortilla Wraps celozrnná LIDL", nEnergy=291.38, nProtein=9.33, nFat=6.00, nCarbohydrate=46.00, nSugar=1.67, nDietaryFiber=0.00),
            "kokosovy_olej" : Ingredient(sName="Kokosový olej", nEnergy=889.80, nProtein=0.00, nFat=98.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "brambory" : Ingredient(sName="Brambory", nEnergy=79.19, nProtein=1.00, nFat=0.00, nCarbohydrate=18.00, nSugar=0.00, nDietaryFiber=1.00),
            "olej_olivovy_extra_panensky" : Ingredient(sName="Olej olivový extra panenský", nEnergy=825.60, nProtein=0.00, nFat=91.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "zakysana_smetana_14_%_pilos" : Ingredient(sName="Zakysaná smetana 14 % Pilos", nEnergy=153.12, nProtein=3.00, nFat=14.00, nCarbohydrate=4.20, nSugar=4.20, nDietaryFiber=0.00),
            "rajce" : Ingredient(sName="Rajče", nEnergy=22.25, nProtein=1.00, nFat=0.00, nCarbohydrate=4.00, nSugar=3.00, nDietaryFiber=2.00),
            "cocka_lagris" : Ingredient(sName="Čočka Lagris", nEnergy=347.85, nProtein=23.00, nFat=0.75, nCarbohydrate=59.00, nSugar=4.00, nDietaryFiber=3.50),
            "vejce_na_tvrdo" : Ingredient(sName="Vejce na tvrdo", nEnergy=150.26, nProtein=12.60, nFat=10.60, nCarbohydrate=1.20, nSugar=0.00, nDietaryFiber=0.00),
            "smakoun_klasik" : Ingredient(sName="Šmakoun Klasik", nEnergy=67.46, nProtein=14.00, nFat=0.18, nCarbohydrate=2.64, nSugar=0.00, nDietaryFiber=2.55),
            "bataty" : Ingredient(sName="Batáty", nEnergy=86.12, nProtein=2.00, nFat=0.00, nCarbohydrate=20.00, nSugar=8.00, nDietaryFiber=3.00),
            "uzena_krkovice" : Ingredient(sName="Uzená krkovice", nEnergy=392.50, nProtein=15.60, nFat=36.60, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "cervena_repa" : Ingredient(sName="Červená řepa", nEnergy=34.93, nProtein=1.57, nFat=0.10, nCarbohydrate=9.53, nSugar=6.70, nDietaryFiber=2.53),
            "jihoceska_niva_50%,_madeta" : Ingredient(sName="Jihočeská Niva 50%, Madeta", nEnergy=348.56, nProtein=22.00, nFat=29.00, nCarbohydrate=0.60, nSugar=0.60, nDietaryFiber=0.00),
            "videnske_parky_80_%_k-cllassic" : Ingredient(sName="Vídeňské párky 80 % K-Cllassic", nEnergy=250.00, nProtein=13.10, nFat=22.00, nCarbohydrate=0.70, nSugar=0.50, nDietaryFiber=0.00),
            "horcice_dijonska" : Ingredient(sName="Hořčice dijonská", nEnergy=161.23, nProtein=7.67, nFat=12.00, nCarbohydrate=3.00, nSugar=1.67, nDietaryFiber=0.00),
            "veprova_kyta" : Ingredient(sName="Vepřová kýta", nEnergy=208.87, nProtein=17.40, nFat=15.40, nCarbohydrate=0.10, nSugar=0.00, nDietaryFiber=0.00),
            "anglicka_slanina_85_%_ceska_chut" : Ingredient(sName="Anglická slanina 85 % Česká chuť", nEnergy=384.44, nProtein=10.88, nFat=37.94, nCarbohydrate=1.18, nSugar=0.29, nDietaryFiber=0.29),
            "lucina" : Ingredient(sName="Lučina", nEnergy=291.40, nProtein=11.00, nFat=27.00, nCarbohydrate=1.00, nSugar=0.00, nDietaryFiber=0.00),
            "madeland_light_30%,_madeta" : Ingredient(sName="Madeland light 30%, Madeta", nEnergy=285.41, nProtein=30.00, nFat=18.24, nCarbohydrate=1.18, nSugar=1.18, nDietaryFiber=0.00),
            "quinoa" : Ingredient(sName="Quinoa", nEnergy=342.60, nProtein=15.00, nFat=5.00, nCarbohydrate=59.00, nSugar=0.00, nDietaryFiber=5.00),
            "brokolice" : Ingredient(sName="Brokolice", nEnergy=37.80, nProtein=3.00, nFat=0.00, nCarbohydrate=6.00, nSugar=2.00, nDietaryFiber=3.00),
            "zampiony" : Ingredient(sName="Žampióny", nEnergy=35.88, nProtein=3.00, nFat=0.00, nCarbohydrate=5.00, nSugar=0.00, nDietaryFiber=2.00),
            "ghi_-_prepustene_maslo" : Ingredient(sName="Ghí - přepuštěné máslo", nEnergy=879.70, nProtein=0.00, nFat=99.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "halloumi_syr" : Ingredient(sName="Halloumi sýr", nEnergy=333.26, nProtein=21.20, nFat=27.00, nCarbohydrate=2.20, nSugar=1.00, nDietaryFiber=0.00),
            "dynova_seminka" : Ingredient(sName="Dýňová semínka", nEnergy=516.00, nProtein=30.00, nFat=49.33, nCarbohydrate=12.00, nSugar=1.33, nDietaryFiber=4.00),
            "porek" : Ingredient(sName="Pórek", nEnergy=39.20, nProtein=2.00, nFat=0.00, nCarbohydrate=7.00, nSugar=3.00, nDietaryFiber=3.00),
            "tvaroh_polotucny_prumer" : Ingredient(sName="Tvaroh polotučný průměr", nEnergy=110.05, nProtein=10.00, nFat=4.00, nCarbohydrate=5.00, nSugar=4.00, nDietaryFiber=0.00),
            "granola_-_krupave_musli_bio_countrylife" : Ingredient(sName="Granola - Křupavé müsli BIO CountryLife", nEnergy=442.60, nProtein=11.00, nFat=15.00, nCarbohydrate=63.00, nSugar=15.00, nDietaryFiber=6.00),
            "kiwi" : Ingredient(sName="Kiwi", nEnergy=65.07, nProtein=1.00, nFat=0.00, nCarbohydrate=14.00, nSugar=9.00, nDietaryFiber=3.00),
            "olej_lneny_franz_josef" : Ingredient(sName="Olej lněný Franz Josef", nEnergy=814.40, nProtein=0.00, nFat=92.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "gnocchi_bramborove_noky_tesco" : Ingredient(sName="Gnocchi bramborové noky Tesco", nEnergy=165.31, nProtein=3.25, nFat=0.25, nCarbohydrate=35.75, nSugar=0.25, nDietaryFiber=1.88),
            "bazalkove_pesto_panzani" : Ingredient(sName="Bazalkové pesto Panzani", nEnergy=326.56, nProtein=3.86, nFat=31.43, nCarbohydrate=7.57, nSugar=0.86, nDietaryFiber=1.57),
            "spenat" : Ingredient(sName="Špenát", nEnergy=18.00, nProtein=2.67, nFat=0.33, nCarbohydrate=3.00, nSugar=1.33, nDietaryFiber=2.00),
            "chleb_zitny" : Ingredient(sName="Chléb žitný", nEnergy=241.62, nProtein=7.60, nFat=1.00, nCarbohydrate=48.40, nSugar=2.40, nDietaryFiber=10.00),
            "hovezi_svickova" : Ingredient(sName="Hovězí svíčková", nEnergy=152.15, nProtein=20.00, nFat=7.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "sadlo_veprove" : Ingredient(sName="Sádlo vepřové", nEnergy=897.80, nProtein=0.00, nFat=99.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "fazolka" : Ingredient(sName="Fazolka", nEnergy=21.89, nProtein=2.20, nFat=0.30, nCarbohydrate=6.30, nSugar=1.70, nDietaryFiber=3.60),
            "kozi_syr_milbona" : Ingredient(sName="Kozí sýr Milbona", nEnergy=387.08, nProtein=25.40, nFat=32.20, nCarbohydrate=0.20, nSugar=0.20, nDietaryFiber=0.00),
            "rukola" : Ingredient(sName="Rukola", nEnergy=24.17, nProtein=2.00, nFat=0.67, nCarbohydrate=2.67, nSugar=0.00, nDietaryFiber=1.67),
            "redkvicky" : Ingredient(sName="Ředkvičky", nEnergy=21.30, nProtein=1.00, nFat=0.00, nCarbohydrate=4.00, nSugar=2.00, nDietaryFiber=2.00),
            "toustovy_chleb_cerealni" : Ingredient(sName="Toustový chléb cereální", nEnergy=252.40, nProtein=9.50, nFat=4.00, nCarbohydrate=41.00, nSugar=3.00, nDietaryFiber=7.00),
            "cocka_cervena_lagris" : Ingredient(sName="Čočka červená Lagris", nEnergy=353.11, nProtein=25.14, nFat=0.86, nCarbohydrate=60.00, nSugar=3.71, nDietaryFiber=1.14),
            "grapefruity" : Ingredient(sName="Grapefruity", nEnergy=44.02, nProtein=1.00, nFat=0.00, nCarbohydrate=10.00, nSugar=6.00, nDietaryFiber=2.00),
            "salat_hlavkovy" : Ingredient(sName="Salát hlávkový", nEnergy=17.46, nProtein=1.00, nFat=0.00, nCarbohydrate=3.00, nSugar=1.00, nDietaryFiber=2.00),
            "vinny_ocet" : Ingredient(sName="Vinný ocet", nEnergy=11.80, nProtein=0.00, nFat=0.00, nCarbohydrate=6.00, nSugar=0.00, nDietaryFiber=0.00),"para_orechy" : Ingredient(sName="Para ořechy", nEnergy=705.53, nProtein=14.00, nFat=67.33, nCarbohydrate=10.67, nSugar=2.67, nDietaryFiber=6.00),
            "bulgur_psenicny" : Ingredient(sName="Bulgur pšeničný", nEnergy=359.57, nProtein=12.00, nFat=1.00, nCarbohydrate=70.00, nSugar=0.00, nDietaryFiber=18.00),
            "cottage" : Ingredient(sName="Cottage", nEnergy=118.89, nProtein=11.07, nFat=7.07, nCarbohydrate=3.07, nSugar=3.07, nDietaryFiber=0.00),
            "seitan_natural_sunfood" : Ingredient(sName="Seitan natural Sunfood", nEnergy=137.32, nProtein=21.00, nFat=2.00, nCarbohydrate=8.00, nSugar=2.00, nDietaryFiber=0.00),
            "zakysana_smetana_15_%_madeta" : Ingredient(sName="Zakysaná smetana 15 % Madeta", nEnergy=172.96, nProtein=3.00, nFat=16.00, nCarbohydrate=4.80, nSugar=4.20, nDietaryFiber=0.00),
            "cheddar_president" : Ingredient(sName="Cheddar Président", nEnergy=412.70, nProtein=25.00, nFat=35.00, nCarbohydrate=0.50, nSugar=0.00, nDietaryFiber=0.00),
            "bazalka_cerstva" : Ingredient(sName="Bazalka čerstvá", nEnergy=23.00, nProtein=3.00, nFat=1.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=2.00),
            "mozzarella_galbani" : Ingredient(sName="Mozzarella Galbani", nEnergy=236.60, nProtein=17.04, nFat=18.00, nCarbohydrate=2.00, nSugar=1.04, nDietaryFiber=0.00),
            "cervena_repa_predvarena" : Ingredient(sName="Červená řepa předvařená", nEnergy=31.96, nProtein=1.20, nFat=0.12, nCarbohydrate=5.80, nSugar=4.72, nDietaryFiber=0.00),
            "balkansky_syr,_madeta" : Ingredient(sName="Balkánský sýr, Madeta", nEnergy=264.60, nProtein=16.00, nFat=22.00, nCarbohydrate=1.27, nSugar=1.27, nDietaryFiber=0.00),
            "knackebrot_zitny_racio" : Ingredient(sName="Knäckebrot žitný Racio", nEnergy=355.50, nProtein=9.00, nFat=2.00, nCarbohydrate=66.00, nSugar=2.00, nDietaryFiber=17.00),
            "basmati_ryze" : Ingredient(sName="Basmati ryze", nEnergy=353.33, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "hovezi_mlete_maso" : Ingredient(sName="Hovezi mlete maso", nEnergy=167.14, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "jarni_cibulka" : Ingredient(sName="Jarni cibulka", nEnergy=26.67, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "tortila_celozrnna" : Ingredient(sName="Tortila celozrnna", nEnergy=280.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "rajcatove_pyre" : Ingredient(sName="Rajcatove pyre", nEnergy=20.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "koriandr_cerstvy" : Ingredient(sName="koriandr cerstvy", nEnergy=16.67, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "barbecue_omacka" : Ingredient(sName="barbecue omacka", nEnergy=135.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "olivovy_olej" : Ingredient(sName="Olivovy olej", nEnergy=800.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "cervena_paprika" : Ingredient(sName="Cervena paprika", nEnergy=33.33, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "kukurice_bounuelle" : Ingredient(sName="Kukurice Bounuelle", nEnergy=76.67, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "jarni_cibulka" : Ingredient(sName="Jarní cibulka", nEnergy=0.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "mascarpone" : Ingredient(sName="Mascarpone", nEnergy=0.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "susena_rajcata" : Ingredient(sName="Sušená rajčata", nEnergy=0.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "kysla_smotana" : Ingredient(sName="Kyslá smotana", nEnergy=0.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "paprika_bila" : Ingredient(sName="Paprika bílá", nEnergy=0.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00),
            "pohanky_kroupa" : Ingredient(sName="Pohanky kroupa", nEnergy=0.00, nProtein=0.00, nFat=0.00, nCarbohydrate=0.00, nSugar=0.00, nDietaryFiber=0.00)
        }

        session.add_all(ingredients.values())
        session.commit()

        meals = []
        workingMeal = Meal(sName = "Rýžové placičky s jablkem a banánem", sType="Snídaně", sInstructions = "Uvaříme rýži v osolené vodě. 1/2 (+-) jablka nastrouháme, 1/2 banánu rozmačkáme a smícháme společně s uvařenou rýží a 1 ks vejce. Získáme směs, ze které vytvarujeme na pečící papír placičky a posypeme každou rozdrcenými mandlemi. Pečeme na 200 stupňů 20 minut.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "40", sUnit = "g", ingredient = ingredients["ryze_jasminova"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["jablko"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "65", sUnit = "g", ingredient = ingredients["banany"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "55", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["mandle"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Osvěžující borůvkový bowl", sType="Snídaně", sInstructions = "Borůvky MRAŽENÉ a kefírové mléko rozmixujeme v mixéru. Dáme do misky a posypeme mandlemi, vlašskými ořechy, semínky a 1/2 banánu.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["boruvky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "250", sUnit = "g", ingredient = ingredients["kefirove_mleko_bile_1,5%_kunin"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["mandle"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["orechy_vlasske"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["slunecnicova_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "60", sUnit = "g", ingredient = ingredients["banany"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Kváskový chléb s budapešťskou pomazánkou", sType="Snídaně", sInstructions = "1 širší plátek kváskového chleba potřeme budapešťskou pomazánkou -> 1/2 tvarohu (zbytek Kubko), 1 lžíce másla, 1/4 zakysané smetany, nakrájená cibulka dle potřeby, kapie (program je nenabízí, proto červená paprika). Červená mleté paprika, sůl, pepř přidáme dle svých chutí.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["kvaskovy_chleb"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "125", sUnit = "g", ingredient = ingredients["jihocesky_tvaroh_polotucny_madeta"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["maslo_80_%_president"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["zakysana_smetana_15_%_kunin"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["cibule"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["paprika_cervena"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "3", sUnit = "g", ingredient = ingredients["paprika_sladka"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Smoothie", sType="Snídaně", sInstructions = "Vše rozmixujeme. 125g tvaroh = 1/2 60g banán = 1/2")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["kefirove_mleko_bile_1,5%_kunin"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "125", sUnit = "g", ingredient = ingredients["jihocesky_tvaroh_polotucny_madeta"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "60", sUnit = "g", ingredient = ingredients["banany"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["chia_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["mrazene_boruvky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["orechy_vlasske"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Banánové smoothie bowl", sType="Snídaně", sInstructions = "Mléko (může být živočišné), kakao, chia a banán (1/2) společně umixujeme do hladka. Směs přemístíme do misky, posypeme nastrouhanou čokoládou (1 ks), ořechy a poklademe plátky banánu (1/2). Ihned podáváme.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "250", sUnit = "g", ingredient = ingredients["mandlove_mleko_dm_bio"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "120", sUnit = "g", ingredient = ingredients["banany"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "15", sUnit = "g", ingredient = ingredients["bio_kakao_horke"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["chia_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["horka_cokolada_lindt_85%"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "15", sUnit = "g", ingredient = ingredients["orechy_vlasske"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Jáhly s mandarinkami", sType="Snídaně", sInstructions = "Jáhly uvaříme a smícháme je 1 ks hořké čokolády, aby se rozpustila. Ozdobíme mandarinkami z plechovky, semínky a ořechy.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "35", sUnit = "g", ingredient = ingredients["jahly"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["horka_cokolada_lindt_85%"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "15", sUnit = "g", ingredient = ingredients["slunecnicova_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["mandarinky_ve_sladkem_nalevu_giana"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["orechy_vlasske"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Ovesná kaše s jogurtem", sType="Snídaně", sInstructions = "V kastrůlku ohřejeme mléko, přidáme do něj 1 ČL chia semínek, necháme si zároveň převařit vodu v konvici. Až bude mléko teplé, přidáte ovesné vločky, zamícháme a přidáme vodu dle potřeby (přidáváme po troškách, ať ji není příliš, kaše pak nebude mít dobrou chuť), mícháme do zhoustnutí. V misce poté kaši smícháme s celým jogurtem 5% tuku. Ozdobíme ovocem a ořechy.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "35", sUnit = "g", ingredient = ingredients["ovesne_vlocky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["mleko_plnotucne_3,5%"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["chia_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "140", sUnit = "g", ingredient = ingredients["recky_jogurt_milko_5%"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["maliny"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "15", sUnit = "g", ingredient = ingredients["orechy_vlasske"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Kváskový chléb s hummusem, šunkou a sýrem", sType="Snídaně", sInstructions = "1 plátek chleba potřeme hummusem, obložíme 2 ks vysokoprocentní šunka a 1 plátek sýru. K tomu ovoce a 1 ks mrkev.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["kvaskovy_chleb"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["hummus_original_yami"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["dusena_sunka_veprova_96%_dulano"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "17", sUnit = "g", ingredient = ingredients["eidam_30_%_blanik"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["jablko"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["mrkev"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Kváskový chléb s hermelínovou pomazánkou", sType="Snídaně", sInstructions = "V první řadě si dáme vařit vajíčko. Mezitím si pokrájíme hermelín na malé kousky (zbytek Kubko), přidáme pokrájené kyselé okurky a dochutíme 1/2 jogurtem a špetkou soli, pepřem ... Na závěr přidáme pokrájené uvařené vajíčko, a všechno společně promícháme a dáme na chvíli vychladit do lednice. Pomazánkou potřeme kváskový chléb.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["kvaskovy_chleb"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "55", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["moravske_okurky_efko"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["hermelin_kral_syru"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["recky_jogurt_0%_tuku_milko"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Těstovinový salát se sušenými rajčaty a mozzarellou", sType="Oběd", sInstructions = "Uvaříme těstoviny (v hotovém +- 85 g), smícháme se sušenými rajčaty (vč. trocha oleje), 1/2 ks mozzarelly (druhá polovina Kubko), listovou zeleninu (nevážíme, odhadem), 1/2 okurka, 1 ks mrkev a semínka, které opražíme na suché pánvi pro lepší chuť. Na konec trošku zakápneme za studena lisovaným olejem. Salát ochutíme dle svých chutí.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["testoviny_panzani"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "40", sUnit = "g", ingredient = ingredients["susena_rajcata_franz_josef"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "60", sUnit = "g", ingredient = ingredients["mozzarella_light_galbani"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["polnicek"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["okurky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["mrkev"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["slunecnicova_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["olej_olivovy"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Poke bowl", sType="Oběd", sInstructions = "Uvaříme rýži (v hotovém stavu +-110g), přendáme do misky a naskládáme na ni čerstvého lososa, avokádo, 1/2 mrkev a kukuřici. Můžeme lehce pokapat sójovou omáčkou.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["basmati_ryze_vitana"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["losos_obecny"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["avokado"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["mrkev"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["kukurice_bonduelle"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["sojova_omacka"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Karbanátky z hovězího masa a zeleniny", sType="Oběd", sInstructions = "Hovězí mleté maso smícháme s 1 ks vejce, 1/2 červené papriky, nastrouhanou 1/2 ks mrkve, 1/2 malé nastrouhané cukety. Osolíme, opepříme, přidáme případně bylinky. Vznikne nám směs, ze které na pečící papír vytvarujeme placky. Pečeme na 200 stupňů, 30 minut. Ke konci pečení potřeme olivovým olejem.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "120", sUnit = "g", ingredient = ingredients["hovezi_maso_mlete"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "55", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["paprika_cervena"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["mrkev"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["cuketa"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["olej_olivovy"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Cuketové placky s tuňákem", sType="Oběd", sInstructions = "Nejprve si oloupej cuketu a najemno nastrouhej. Posol a nech 10 minut odstát.Mezitím si nakrájej cibuli (nemusí být) na kostičky a česnek na plátky. Na řepkovém (můžeš kokosový) oleji restuj dozlatova. Cuketu důkladně vymačkej. Poté přidej vejce (2ks), orestovanou cibuli s česnekem, špaldovou mouku a tuňáka (můžeš i nemusíš dávat do těsta), kterého jsi předem zbavila šťávy. Směs osol, opepři a důkladně zamíchej. Orestuj na pánvi do zlatova.TIP: Placky je možné dát i do trouby. Stačí péct při 200 stupních z každé strany cca. 10 minut")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "200", sUnit = "g", ingredient = ingredients["cuketa"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["spaldova_mouka_celozrnna"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "112", sUnit = "g", ingredient = ingredients["tunak_rio_mare_ve_vlastni_stave"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["olej_repkovy_aro"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "110", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["cibule"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["cesnek"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Tofu s rýžovými nudlemi", sType="Oběd", sInstructions = "Rýžové nudle dáme vařit do osolené vody (dle návodu na obalu). Nakrájené tofu na kostičky lehce osmahneme na sucho na pánvičce na mírném ohni. V mističce si připravíme zálivku: med, citron, olej, sůl. Uvařené nudle chvíli orestujeme spolu s tofu, smícháme, přendáme na talíř/do misky, zalejeme zálivkou, smícháme a též smícháme s 1ks nastrouhanou mrkví.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["ryzove_nudle"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "120", sUnit = "g", ingredient = ingredients["tofu_natural"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["mrkev"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["med"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["citrony"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["olej_olivovy"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Kváskový chléb s quacamole", sType="Oběd", sInstructions = "Avokádo rozmačkáme v misce, přidáme nakrájenou červenou cibuli, 1/2 balení cherry rajčátek. Zakápneme citronovou šťávou, osolíme, zamícháme. Podáváme jako pomazánku na 1 plátek žitný chléb.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "120", sUnit = "g", ingredient = ingredients["avokado"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["cibule_cervena"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "125", sUnit = "g", ingredient = ingredients["rajcata_cherry"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["kvaskovy_chleb"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Boloňské špagety", sType="Oběd", sInstructions = "Mleté maso osmahneš na suché pánvi, až bude hotové přidáš boloňskou omáčku, necháš ohřát, přidáš uvařené špagety (150g +- v hotovém) a na talíři posypeš nastrouhaným sýrem.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["hovezi_maso_mlete"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["makarony,_spagety"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["free_form_bolonska_omacka_tesco"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["parmezan"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Quesadilla s mozzarellou a zeleninou", sType="Oběd", sInstructions = "Na talíři si rozprostřeme 1 ks tortilly (pozor, té menší!, jsou i velikosti o 120g), naskládáme na její jednu půlku na sebe ledový salát, nakrájená rajčátka, kukuřici, nakrájenou na plátky light mozzarellu a druhou polovinou tortilly směs zaděláme a dáme na kontaktní gril, do toustovače, na pánev či do kleští na gril a následně do trouby a na pár minutek (1-3) z obou stran dáme opéct. K tomu 1/2 kelímek řeckého jogurtu. Buď potřeme nebo do jogurtu namáčíme.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "60", sUnit = "g", ingredient = ingredients["tortilla_wraps_(crusticroc)"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["salat_ledovy"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["rajcata_cherry"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["kukurice_bonduelle"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "120", sUnit = "g", ingredient = ingredients["mozzarella_light_galbani"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["bio_recky_jogurt_bily_milko_5_%"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Tortilla s hummusem a míchaný, vajíčkem", sType="Oběd", sInstructions = "Na 1ks menší tortilly (před si ji ohřejeme v mikrovlnce 20s) rozetřeme hummus. Na pánvičce potřené kokosovým olejem osmahneme 1ks vejce (míchané). To rozložíme též do tortily na její prostředek, dále přidáme ledový salát, rajčátka a nastrouhanou mrkev.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "60", sUnit = "g", ingredient = ingredients["tortilla_wraps_celozrnna_lidl"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["hummus_original_yami"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "55", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["kokosovy_olej"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["salat_ledovy"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["rajcata_cherry"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["mrkev"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Opečené tofu s pečenými brambory, dip ze zakysané smetany", sType="Večeře", sInstructions = "Pokrájené a očistěné brambory (lze zaměnit za batáty) zakápneme trochou olivovým olejem, přidáme sůl a bylinky (libovolně) a pečeme v troubě dozlatova. Podáváme s na pánvi opečeným tofu (na sucho) a dipem ze zakysky (libovolně přidáme česnek, sůl, pepř, bylinky). K tomu dále 1ks rajče.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["brambory"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["olej_olivovy_extra_panensky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "170", sUnit = "g", ingredient = ingredients["tofu_natural"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["zakysana_smetana_14_%_pilos"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["rajce"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Čočka se šmakounem a vejcem", sType="Večeře", sInstructions = "Uvaříme čočku, 2 ks vejce. Na lehce potřené pánvi olejem osmahneme 1 ks šmakouna, druhý ks Kubko.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "40", sUnit = "g", ingredient = ingredients["cocka_lagris"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["vejce_na_tvrdo"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["kokosovy_olej"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "110", sUnit = "g", ingredient = ingredients["smakoun_klasik"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Pečený losos s pečenými batáty", sType="Večeře", sInstructions = "Lososa potřeme na pečícím papíru olejem, ochutíme dle svých chutí (sůl, citron, bylinky...) a přihodíme k němu batáty (lze zaměnit s bramborami).")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "120", sUnit = "g", ingredient = ingredients["losos_obecny"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["olej_olivovy"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "180", sUnit = "g", ingredient = ingredients["bataty"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Avokádové špagety se sušenými rajčaty", sType="Večeře", sInstructions = "umixujeme dohladka avokádo , ochutíme ho solí , pepřem nebo chilli a trošičkou citronové šťávy, ale opravdu jen pár kapek pro osvěžení chuti. V malé pánvičce si opečeme nakrájená rajčátka, jelikož jsou již v oleji a avokádo je také nabité tukem, opečeme je bez dalšího přidávání oleje nebo másla. Poté ztlumíme teplotu, vmícháme avokádo, nastrouhaný sýr a čerstvou bazalku. Vhodíme uvařené těstoviny a vše smícháme, můžeme trošku naředit vodou z těstovin. Podáváme ozdobené bazalkou.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["makarony,_spagety"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["susena_rajcata_franz_josef"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "80", sUnit = "g", ingredient = ingredients["avokado"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["parmezan"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Bramboráčky", sType="Večeře", sInstructions = "Brambory oloupeme, nastrouháme a smícháme s 1 ks vejce, ovesnými vločkami, nakrájenou kvalitní zauzenou šunkou/salámem na malé kostičky a stroužkem česneku. Směs ochutíme majoránkou a dle potřeby sůl + pepř. Ze směsi na pečící papír vytvarujeme kolečka. Pečeme na 200 stupňů 30 minut.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "200", sUnit = "g", ingredient = ingredients["brambory"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "55", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["ovesne_vlocky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["uzena_krkovice"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["cesnek"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Langoše ze špaldové mouky a kefíru", sType="Večeře", sInstructions = "Smícháme mouku, kefír a 1 PL olivového oleje. Vytvarujeme na pečící papír menší placičky, pečeme 15 minut na 180 stupňů. Po upečení potřeme česnekem (ale nemusíš), zakysanou smetanou a posypeme nastrouhaným eidamem. Jsou to spíše takové akoze langose, placky se nafouknou, tak se nelekat a pochutnat si i tak. :)")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "80", sUnit = "g", ingredient = ingredients["spaldova_mouka_celozrnna"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "80", sUnit = "g", ingredient = ingredients["kefirove_mleko_bile_1,5%_kunin"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["olej_olivovy"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["zakysana_smetana_15_%_kunin"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["cesnek"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["eidam_30_%_blanik"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Zapečená řepa s nivou a vlašskými ořechy", sType="Večeře", sInstructions = "pečící papír, posypeme každé kolečko nastrouhanou nivou a na každé kolečko dáme vlašský ořech. Poté dáme do trouby zapéct na 180 stupňů a vyndáme až bude niva do zlatova (cca 30 minut).")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "300", sUnit = "g", ingredient = ingredients["cervena_repa"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["jihoceska_niva_50%,_madeta"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "25", sUnit = "g", ingredient = ingredients["orechy_vlasske"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Párky s kváskovým chlebem", sType="Večeře", sInstructions = "2 nožičky kvalitních párků s 1 plátkem kváskového chleba s hořčicí (klidně kečup, záleží co máš ráda). K tomu zelenina.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["videnske_parky_80_%_k-cllassic"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["horcice_dijonska"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["kvaskovy_chleb"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["paprika_cervena"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Vepřové ražniči s bramborami", sType="Večeře", sInstructions = "Na plech rozprostřeme alobal, vyskládáme na plech (alobal) nakrájené brambory na tenké plátky a vrstvíme maso též nakrájené na plátky, dále přidáme nakrájenou anglickou slaninu (2 ks) a papriku. Nakonec navrstvíme hodně cibule, posypeme grilovacím kořením, zakryjeme alobalem a pečeme na 200°C asi 60 minut.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["veprova_kyta"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["cibule"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "34", sUnit = "g", ingredient = ingredients["anglicka_slanina_85_%_ceska_chut"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["paprika_cervena"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["brambory"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Kváskový chléb se šunkou a sýrem", sType="Snídaně", sInstructions = "1 plátek kváskového chleba potřeme Lučinou, obložíme 2 ks plátky vysokoprocentní šunky, 1 plátkem sýru. K tomu 1ks mrkev a připíjíme 300 ml kefíru.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["kvaskovy_chleb"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["lucina"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["dusena_sunka_veprova_96%_dulano"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "17", sUnit = "g", ingredient = ingredients["madeland_light_30%,_madeta"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["mrkev"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "300", sUnit = "g", ingredient = ingredients["kefirove_mleko_bile_1,5%_kunin"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Quinoa salát s halloumi sýrem", sType="Oběd", sInstructions = "Quinoa uvedena v syrovém stavu (v hotovém +- 90g). Brokolici můžeme dát na 5 minut vařit. Na ghí (nebo kokosovém oleji) osmahneme nakrájené žampiony, tak stejně osmahneme na plátky nakrájený Halloumi sýr (můžeme na jedné pánvi). Na talíři vše buď smícháme nebo vyskládáme vedle sebe, to už záleží na tobě. Na konec přidáme hrst polníčku či jiné listové zeleniny a posypeme semínky.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["quinoa"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["brokolice"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["zampiony"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["ghi_-_prepustene_maslo"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["halloumi_syr"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["polnicek"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "15", sUnit = "g", ingredient = ingredients["dynova_seminka"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Tofu s rýží a kukuřicí", sType="Večeře", sInstructions = "Tofu nakrájíme na kostičky a osmahneme na sucho na pánvi. Rýže je uvedena v syrovém stavu, v hotovém potom +- 110g. Talíř doplníme dále o kukuřici, nakrájený pórek (od oka) a semínka. Ochutíme dle svých chutí.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["tofu_natural"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["basmati_ryze_vitana"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["kukurice_bonduelle"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["slunecnicova_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["porek"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Polotučný tvaroh s kakaem a mandlovým mlékem", sType="Snídaně", sInstructions = "Do misky si dáme celý tvaroh, mléko (může být živočišné!), semínka, kakao a smícháme. Ozdobíme musli a ovocem.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "250", sUnit = "g", ingredient = ingredients["tvaroh_polotucny_prumer"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["mandlove_mleko_dm_bio"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["chia_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["bio_kakao_horke"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["granola_-_krupave_musli_bio_countrylife"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["kiwi"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Těstovinový salát s tuňákem", sType="Oběd", sInstructions = "Těstoviny v hotovém +- 85g. Šťávu z tuňáka slejeme a vše smícháme dohromady - hrst polníčku či jiné listové zeleniny, rajčata, oříšky, semínka a těstoviny. Na konec zakápneme za studena lisovaným olejem. Ochutíme dle svých chutí.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["testoviny_panzani"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "112", sUnit = "g", ingredient = ingredients["tunak_rio_mare_ve_vlastni_stave"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["polnicek"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["rajcata_cherry"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["orechy_vlasske"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["slunecnicova_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["olej_lneny_franz_josef"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Gnochi s bazalkovým pestem a parmazánem", sType="Večeře", sInstructions = "Uvaříme gnochi, na pánvi mezitím ohřejeme bazalkové pesto a spolu s ním také mírně podusíme cherry rajčátka, uvařené gnochi k němu přidáme, zamícháme a na talíři posypeme parmazánem.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "80", sUnit = "g", ingredient = ingredients["gnocchi_bramborove_noky_tesco"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["bazalkove_pesto_panzani"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "125", sUnit = "g", ingredient = ingredients["rajcata_cherry"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["parmezan"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Míchaná vajíčka s baby špenátem a žitným chlebem", sType="Snídaně", sInstructions = "Na kokosovém oleji osmahneme 2 míchaná vejce, přidáme na pánev hrst baby špenátu - vše mícháme dohromady. K tomu 1 plátek žitného chleba (může být váš domácí) potřený lučinou + přikusujeme 1/2 jablko.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "110", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["kokosovy_olej"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["spenat"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["chleb_zitny"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["lucina"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "75", sUnit = "g", ingredient = ingredients["jablko"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Hovězí steak s fazolkami a americkými bramborami", sType="Oběd", sInstructions = "Na pánvi s rozehřátým sádlem na prudko opečeš maso a poté jej dáš spolu s bramborami do trouby. Brambory si včetně slupky jen omyješ, nakrájíš a dáš na sucho vedle masa. Na pánvi po mase poté osmahneš fazolky s česnekem - 1 stroužek.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["hovezi_svickova"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["sadlo_veprove"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["brambory"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["fazolka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["cesnek"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Omeleta se špenátem a kozím sýrem", sType="Večeře", sInstructions = "Vajíčka (2) rozmixujeme spolu s cca hrstí špenátu, přidáme sůl a pepř. Smažíme na kokosovém oleji. Hotovou omeletu naplníme kozím sýrem, pokrájenými ředkvičkami a rukolou.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "110", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["kokosovy_olej"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["spenat"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["kozi_syr_milbona"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["rukola"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["redkvicky"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Tousty", sType="Snídaně", sInstructions = "2 ks toustový chléb (=1 zapečený toust), potřeme lučinou, do toustu: 1 plátek sýr, 2 plátky vysokoprocentní šunky a zapečeme. K tomu 1 červená paprika (+-) a kefírové mléko.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "40", sUnit = "g", ingredient = ingredients["toustovy_chleb_cerealni"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "40", sUnit = "g", ingredient = ingredients["lucina"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "17", sUnit = "g", ingredient = ingredients["madeland_light_30%,_madeta"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["dusena_sunka_veprova_96%_dulano"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["paprika_cervena"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "300", sUnit = "g", ingredient = ingredients["kefirove_mleko_bile_1,5%_kunin"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Čočkový salát s avokádem a grapefruitem", sType="Oběd", sInstructions = "Avokádo nakrájíme na kostičky, grapefruit zbavíme slupky vč. vnitřních hořkých blanek a zbylou vnitřní dužinu nakrájíme. 1 ks vejce vařené můžeme též nakrájet nebo rozkrojit na půl a na konec na salát položit. Hlávkový salát natrháme a vše vložíme do mísy s vychladlou čočkou (v hotovém 100 g+-). Důkladně smícháme ingredience na zálivku (ocet, med, sůl, pepř, limetka) a zalijeme jím připravený salát.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "35", sUnit = "g", ingredient = ingredients["cocka_cervena_lagris"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "90", sUnit = "g", ingredient = ingredients["avokado"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["grapefruity"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["vejce_na_tvrdo"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["salat_hlavkovy"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["vinny_ocet"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["med"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Tuňák, avokádo, rajče, žitný chléb", sType="Večeře", sInstructions = "Do misky si dáme 1 plechovku tuňáka (olej/vodu slijeme), nakrájené avokádo, sušená rajčata, ochutíme dle svých chutí (sůl, pepř, ..) a k tomu 1 plátek žitného chleba.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "112", sUnit = "g", ingredient = ingredients["tunak_rio_mare_ve_vlastni_stave"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["avokado"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["susena_rajcata_franz_josef"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["chleb_zitny"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Jogurt s oříšky, ovocem a semínky", sType="Snídaně", sInstructions = "Jogurt smícháme s medem a semínky. Ozdobíme ovocem, oříšky a zdravým müsli.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "140", sUnit = "g", ingredient = ingredients["recky_jogurt_milko_5%"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["chia_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["med"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["boruvky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "15", sUnit = "g", ingredient = ingredients["para_orechy"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["granola_-_krupave_musli_bio_countrylife"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Bulgurový salát se zeleninou a cottage sýrem", sType="Oběd", sInstructions = "Uvařený bulgur (+-130g v hotovém stavu) smícháme s pokrájenou zeleninou, 1/2 cottage sýrem, semínky a dochutíme dle libosti kořením či bylinkami. Na konec zakápneme za studena lisovaným olejem.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["bulgur_psenicny"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["salat_ledovy"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["kukurice_bonduelle"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "40", sUnit = "g", ingredient = ingredients["susena_rajcata_franz_josef"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "75", sUnit = "g", ingredient = ingredients["cottage"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["slunecnicova_seminka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["olej_olivovy_extra_panensky"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Grilovaný seitan s pečenou zeleninou", sType="Večeře", sInstructions = "Brambory, papriku a cibuli očistíme a nakrájíme na menší kousky. Zeleninu zakápneme olivovým olejem a ochutíme dle svých chutí. Seitan nakrájíme na asi 1 cm silné plátky a též dochutíme dle svých chutí. Oboje grilujeme nebo pečeme v troubě, zelenina potřebuje více času, seitan méně. K tomu 1/4 zakysané smetany.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["brambory"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "100", sUnit = "g", ingredient = ingredients["paprika_cervena"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["cibule_cervena"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["olej_olivovy_extra_panensky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "130", sUnit = "g", ingredient = ingredients["seitan_natural_sunfood"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["zakysana_smetana_15_%_madeta"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Kváskový chléb s volským okem", sType="Snídaně", sInstructions = "Plátek kváskového chleba potřeme lučinou, obložíme plátkem chedaru, na kokosovém oleji osmahneme volské oko, položíme na chleba. K tomu červená paprika.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["kvaskovy_chleb"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["lucina"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["cheddar_president"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "55", sUnit = "g", ingredient = ingredients["vejce_slepici_m"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["kokosovy_olej"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "150", sUnit = "g", ingredient = ingredients["paprika_cervena"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Caprese s toustovým chlebem", sType="Oběd", sInstructions = "2 ks rajčata a mozzarellu nakrájíme na tenké plátky, zakápneme olivovým olejem a posypeme bazalkou. K tomu přikusujeme 1 ks opečený toustový chléb.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "200", sUnit = "g", ingredient = ingredients["rajce"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["olej_olivovy_extra_panensky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["bazalka_cerstva"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "125", sUnit = "g", ingredient = ingredients["mozzarella_galbani"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["toustovy_chleb_cerealni"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Červená řepa s balkánským sýrem a zakysanou smetanou", sType="Večeře", sInstructions = "Vařenou červenou řepu nakrájíme na kostičky, smícháme s nakrájeným balkánským sárem a1/4 zakysané smetany. Můžeme přidat česnek. Dochutíme dle svých vlastních chutí a přikusujeme 2 ks knäckebrot.")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "250", sUnit = "g", ingredient = ingredients["cervena_repa_predvarena"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "55", sUnit = "g", ingredient = ingredients["balkansky_syr,_madeta"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["zakysana_smetana_15_%_kunin"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["cesnek"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "10", sUnit = "g", ingredient = ingredients["olej_olivovy_extra_panensky"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["knackebrot_zitny_racio"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Buritto", sType="Oběd", sInstructions = "")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["basmati_ryze"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "70", sUnit = "g", ingredient = ingredients["hovezi_mlete_maso"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "15", sUnit = "g", ingredient = ingredients["jarni_cibulka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "60", sUnit = "g", ingredient = ingredients["tortila_celozrnna"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["rajcatove_pyre"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "6", sUnit = "g", ingredient = ingredients["koriandr_cerstvy"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["barbecue_omacka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "5", sUnit = "g", ingredient = ingredients["olivovy_olej"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "25", sUnit = "g", ingredient = ingredients["cibule"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["cervena_paprika"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "30", sUnit = "g", ingredient = ingredients["kukurice_bounuelle"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Tuňáková pomazánka s žitným chlebem", sType="Snídaně", sInstructions = "")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "25", sUnit = "g", ingredient = ingredients["jarni_cibulka"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "60", sUnit = "g", ingredient = ingredients["mascarpone"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "8", sUnit = "g", ingredient = ingredients["susena_rajcata"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "12", sUnit = "g", ingredient = ingredients["kysla_smotana"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "20", sUnit = "g", ingredient = ingredients["tunak_rio_mare_ve_vlastni_stave"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["paprika_bila"]))
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "60", sUnit = "g", ingredient = ingredients["kvaskovy_chleb"]))
        meals.append(workingMeal)
        workingMeal = Meal(sName = "Pohanka s kysaným zelím, tempehem a tahini", sType="Oběd", sInstructions = "")
        workingMeal.ingredients.append(MealIngredientMap(nQuantity = "50", sUnit = "g", ingredient = ingredients["pohanky_kroupa"]))
        meals.append(workingMeal)

        session.add_all(meals)
        session.commit()

        planGroups = {
            "Pondelok" : PlanGroup(sName = "Pondelok"),
            "Utorok" : PlanGroup(sName = "Utorok"),
            "Streda" : PlanGroup(sName = "Streda"),
            "Stvrtok" : PlanGroup(sName = "Stvrtok"),
            "Piatok" : PlanGroup(sName = "Piatok"),
            "Sobota" : PlanGroup(sName = "Sobota"),
            "Nedela" : PlanGroup(sName = "Nedela"),
        }

        session.add_all(planGroups.values())

        planList = []
        for group in planGroups.values():
                planList.append(Plan(group = group, sName = "Raňajky"))
                planList.append(Plan(group = group, sName = "Obed"))
                planList.append(Plan(group = group, sName = "Večera"))

        session.add_all(planList)
        session.commit()

        # Add Tags
        tags = {
            "vegetarian": Tag(sName="Vegetarian", sColor="#00FF00"),
            "vegan": Tag(sName="Vegan", sColor="#008000"),
            "gluten_free": Tag(sName="Bezlepkové", sColor="#FFFF00"),
            "breakfast": Tag(sName="Raňajky", sColor="#FFA500"),
            "dinner": Tag(sName="Večera", sColor="#0000FF"),
            "lunch": Tag(sName="Obed", sColor="#FF0000"),
        }
        session.add_all(tags.values())
        session.commit()

        meal = session.query(Meal).filter(Meal.sName == "Rýžové placičky s jablkem a banánem").first()
        if meal:
            meal.tags.append(MealTagMap(tag=tags["breakfast"]))
            meal.tags.append(MealTagMap(tag=tags["vegetarian"]))
            meal.tags.append(MealTagMap(tag=tags["gluten_free"]))
            
        meal = session.query(Meal).filter(Meal.sName == "Osvěžující borůvkový bowl").first()
        if meal:
            meal.tags.append(MealTagMap(tag=tags["breakfast"]))
            meal.tags.append(MealTagMap(tag=tags["vegetarian"]))
            
        session.commit()

        # Add default User
        if not session.query(User).filter(User.sUsername == "default").first():
            default_user = User(sUsername="default")
            session.add(default_user)
            session.commit()