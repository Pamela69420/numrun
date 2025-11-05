# 📱 JAK ZROBIĆ APK - INSTRUKCJA KROK PO KROKU

## 🎯 Najłatwiejsza metoda (5 minut!)

### **Metoda: PWA Builder** ⭐

Nie musisz niczego instalować! Wszystko przez przeglądarkę.

---

## 📋 KROK 1: Opublikuj grę online (GitHub Pages)

### A. Jeśli masz już repozytorium na GitHub:

1. **Upewnij się, że zmiany są na branchu main:**
   ```bash
   git checkout main
   git merge claude/analyze-code-011CUpZvppS4S6Fc1A46M9g3
   git push origin main
   ```

2. **Włącz GitHub Pages:**
   - Wejdź na: https://github.com/Pamela69420/numrun
   - Kliknij `Settings` → `Pages`
   - W sekcji `Source` wybierz: `Deploy from a branch`
   - Branch: `main` → Folder: `/ (root)`
   - Kliknij `Save`
   - Poczekaj 1-2 minuty

3. **Sprawdź czy działa:**
   - Twoja gra będzie dostępna pod: `https://pamela69420.github.io/numrun/`
   - Otwórz w przeglądarce i sprawdź

### B. Alternatywa: Netlify (jeszcze łatwiej!)

1. Wejdź na: https://app.netlify.com/drop
2. Przeciągnij całą folder `numrun` na stronę
3. Gotowe! Dostaniesz link typu: `https://random-name.netlify.app`

---

## 📋 KROK 2: Wygeneruj APK przez PWA Builder

1. **Otwórz PWA Builder:**
   - Wejdź na: https://www.pwabuilder.com/

2. **Wpisz URL swojej gry:**
   - W pole wpisz: `https://pamela69420.github.io/numrun/`
   - Lub Twój link z Netlify
   - Kliknij `Start`

3. **Poczekaj na analizę:**
   - PWA Builder sprawdzi Twoją aplikację
   - Powinieneś zobaczyć wysokie wyniki (Twoja gra jest już PWA!)

4. **Przejdź do budowania:**
   - Kliknij zakładkę `Publish` (góra strony)
   - Wybierz `Android`

5. **Wypełnij ustawienia Android:**
   ```
   Package ID: com.numrun.app
   App name: NumRun
   Launcher name: NumRun
   Theme color: #667eea
   Background color: #667eea
   Icon URL: (zostaw domyślną lub wklej URL do ikony)
   ```

6. **Wybierz opcje:**
   - Signing key: `New` (jeśli pierwsza aplikacja)
   - Target SDK: `34` (najnowsza)
   - Min SDK: `21`

7. **Wygeneruj APK:**
   - Kliknij `Generate`
   - Poczekaj 30-60 sekund
   - Kliknij `Download` gdy będzie gotowe

8. **Co dostaniesz:**
   - Plik ZIP zawierający:
     - `app-release-signed.apk` - gotowy do instalacji!
     - `signing-key.keystore` - zachowaj do aktualizacji!
     - `signing-key-info.txt` - hasło i dane

---

## 📋 KROK 3: Zainstaluj APK na telefonie

### Metoda A: Przez USB

1. **Podłącz telefon do komputera**
2. **Skopiuj** `app-release-signed.apk` na telefon
3. **Na telefonie:**
   - Otwórz Menedżer plików
   - Znajdź plik APK
   - Kliknij → może pojawić się prośba o pozwolenie
   - Włącz `Instalowanie z nieznanych źródeł` (dla Menedżera plików)
   - Kliknij `Zainstaluj`

### Metoda B: Przez email/Google Drive

1. **Wyślij APK do siebie:**
   - Email, Google Drive, Dropbox, etc.
2. **Na telefonie:**
   - Pobierz APK
   - Kliknij na pobrany plik
   - Pozwól na instalację z nieznanych źródeł
   - Zainstaluj

### Metoda C: Przez ADB (dla zaawansowanych)

```bash
# Zainstaluj ADB (Android Debug Bridge)
adb install app-release-signed.apk
```

---

## 🎉 GOTOWE!

Teraz powinieneś mieć **NumRun** na swoim telefonie Android!

---

## 🏪 BONUS: Publikacja w Google Play Store

Jeśli chcesz opublikować grę w sklepie:

1. **Stwórz konto:**
   - https://play.google.com/console
   - Koszt: $25 jednorazowo (na zawsze)

2. **Utwórz aplikację:**
   - `Wszystkie aplikacje` → `Utwórz aplikację`
   - Nazwa: NumRun
   - Język: Polski
   - Typ: Gra
   - Kategoria: Edukacja

3. **Wypełnij wymagane dane:**
   - **Karta w sklepie:**
     - Krótki opis (80 znaków)
     - Pełny opis (4000 znaków)
     - Zrzuty ekranu (min. 2 na telefon)
     - Grafika prezentująca (1024x500px)
     - Ikona aplikacji (512x512px)

   - **Klasyfikacja treści:**
     - Wypełnij kwestionariusz (edukacja, brak przemocy)

   - **Docelowi odbiorcy:**
     - Wiek: Wszyscy

   - **Polityka prywatności:**
     - URL do polityki (można użyć generatora online)

4. **Prześlij APK:**
   - `Wersje` → `Wydania` → `Utwórz nowe wydanie`
   - Przeciągnij `app-release-signed.apk`
   - Nazwa wersji: `1.0.0`
   - Kod wersji: `1`

5. **Wyślij do weryfikacji:**
   - Sprawdź wszystkie sekcje (powinny być zielone)
   - Kliknij `Wyślij do weryfikacji`
   - Czas weryfikacji: 2-7 dni

---

## ⚠️ WAŻNE!

### Zachowaj pliki:
- `signing-key.keystore` - **NIGDY GO NIE GUB!**
- `signing-key-info.txt` - hasło do keystore

Bez nich **nie będziesz mógł zaktualizować** aplikacji w przyszłości!

### Bezpieczeństwo:
- Zapisz keystore w co najmniej 2 miejscach (komputer + chmura)
- Nie udostępniaj publicznie
- Zapisz hasło w menedżerze haseł

---

## 🐛 Rozwiązywanie problemów

### Problem: "Nie można zainstalować aplikacji"
**Rozwiązanie:**
- Włącz `Nieznane źródła` w ustawieniach
- Sprawdź czy masz wystarczająco miejsca
- Upewnij się, że APK jest poprawnie pobrany

### Problem: "Aplikacja się nie otwiera"
**Rozwiązanie:**
- Odinstaluj i zainstaluj ponownie
- Sprawdź czy masz Androida 5.0+ (API 21+)
- Wyczyść cache aplikacji

### Problem: PWA Builder pokazuje błędy
**Rozwiązanie:**
- Sprawdź czy strona jest dostępna przez HTTPS
- Upewnij się, że manifest.json jest dostępny
- Sprawdź Service Worker (sw.js)

### Problem: APK jest zbyt duży
**Rozwiązanie:**
- PWA Builder generuje ~5-10 MB
- Jeśli większy, użyj Bubblewrap (3-7 MB)
- Skompresuj obrazy SVG

---

## 📞 Potrzebujesz pomocy?

1. Zobacz `BUILD_APK.md` - szczegółowa dokumentacja
2. PWA Builder docs: https://docs.pwabuilder.com/
3. GitHub Issues: Zgłoś problem w repozytorium

---

## 🎮 TESTOWANIE

Przed publikacją przetestuj:
- [ ] Instalacja APK działa
- [ ] Gra się uruchamia
- [ ] Wszystkie tryby działają (Szybka Runda, Relaks, Daily)
- [ ] Ranking działa (jeśli online)
- [ ] Logowanie/Rejestracja działa
- [ ] Gra działa offline (PWA)
- [ ] Osiągnięcia się odblokowują
- [ ] Zapisywanie postępów działa

---

## ✅ Checklist publikacji

Przed wysłaniem do Google Play:

- [ ] APK działa na co najmniej 2 urządzeniach
- [ ] Przetestowano wszystkie funkcje
- [ ] Przygotowano zrzuty ekranu (min. 4)
- [ ] Napisano opisy (krótki + pełny)
- [ ] Stworzono ikonę 512x512px
- [ ] Stworzono grafikę prezentującą 1024x500px
- [ ] Napisano politykę prywatności
- [ ] Wypełniono klasyfikację treści
- [ ] Sprawdzono czy nazwa "NumRun" jest dostępna
- [ ] Zachowano keystore w bezpiecznym miejscu

---

**Powodzenia! 🚀**

Twoja gra jest gotowa do publikacji!
