# 📱 Jak zbudować APK dla NumRun

Ten przewodnik krok po kroku pomoże Ci stworzyć APK (plik instalacyjny dla Android) z gry NumRun.

## 🎯 Metody budowania APK

### **Metoda 1: Capacitor (Zalecana) ⭐**

Capacitor to nowoczesne narzędzie od twórców Ionic do konwersji PWA na natywne aplikacje.

#### Wymagania:
- Node.js (v16+)
- npm lub yarn
- Android Studio
- Java JDK 17+

#### Kroki:

1. **Zainstaluj zależności:**
   ```bash
   npm install
   ```

2. **Dodaj platformę Android:**
   ```bash
   npx cap add android
   ```

3. **Zsynchronizuj pliki:**
   ```bash
   npx cap sync
   ```

4. **Otwórz w Android Studio:**
   ```bash
   npx cap open android
   ```

5. **W Android Studio:**
   - Kliknij `Build` → `Build Bundle(s) / APK(s)` → `Build APK(s)`
   - Poczekaj na zakończenie kompilacji
   - APK znajdziesz w: `android/app/build/outputs/apk/debug/app-debug.apk`

#### Budowanie z linii poleceń:

**Debug APK:**
```bash
npm run build:apk
```

**Release APK (podpisany):**
```bash
npm run build:release
```

---

### **Metoda 2: PWA Builder (Najłatwiejsza) 🚀**

PWA Builder to internetowe narzędzie - **NIE wymaga instalacji**!

#### Kroki:

1. **Opublikuj grę online** (np. na GitHub Pages, Netlify, Vercel)

2. **Przejdź do:** https://www.pwabuilder.com/

3. **Wpisz URL swojej gry** (np. `https://yourusername.github.io/numrun`)

4. **Kliknij "Start"** - PWA Builder przeanalizuje Twoją aplikację

5. **Wybierz "Publish"** → **"Android"**

6. **Wypełnij dane:**
   - Package ID: `com.numrun.app`
   - App name: `NumRun`
   - Launcher name: `NumRun`

7. **Kliknij "Generate"** - pobierz paczkę

8. **Rozpakuj i podpisz:**
   ```bash
   # Wejdź do folderu
   cd pwa-builder-android

   # Podpisz APK
   jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
     -keystore my-release-key.keystore app-release-unsigned.apk alias_name
   ```

---

### **Metoda 3: Bubblewrap (Oficjalne narzędzie Google)**

#### Wymagania:
- Node.js
- Android SDK

#### Kroki:

1. **Zainstaluj Bubblewrap:**
   ```bash
   npm install -g @bubblewrap/cli
   ```

2. **Zainicjuj projekt:**
   ```bash
   bubblewrap init --manifest https://yourdomain.com/manifest.json
   ```

3. **Zbuduj APK:**
   ```bash
   bubblewrap build
   ```

4. **APK znajdziesz w:** `./app-release-signed.apk`

---

## 🔑 Podpisywanie APK dla Google Play

Aby opublikować w Google Play Store, musisz podpisać APK:

### 1. Stwórz keystore:
```bash
keytool -genkey -v -keystore numrun-release-key.keystore \
  -alias numrun -keyalg RSA -keysize 2048 -validity 10000
```

### 2. Podpisz APK:
```bash
jarsigner -verbose -sigalg SHA256withRSA -digestalg SHA-256 \
  -keystore numrun-release-key.keystore app-release-unsigned.apk numrun
```

### 3. Zoptymalizuj APK:
```bash
zipalign -v 4 app-release-unsigned.apk numrun-release.apk
```

---

## 📦 Konfiguracja ikony i splash screen

### Ikona aplikacji:

Umieść ikony w `android/app/src/main/res/`:
- `mipmap-mdpi/ic_launcher.png` (48x48px)
- `mipmap-hdpi/ic_launcher.png` (72x72px)
- `mipmap-xhdpi/ic_launcher.png` (96x96px)
- `mipmap-xxhdpi/ic_launcher.png` (144x144px)
- `mipmap-xxxhdpi/ic_launcher.png` (192x192px)

### Splash screen:

Edytuj `android/app/src/main/res/values/styles.xml`:
```xml
<style name="AppTheme.NoActionBarLaunch" parent="AppTheme.NoActionBar">
    <item name="android:background">@drawable/splash</item>
</style>
```

---

## 🐛 Rozwiązywanie problemów

### Problem: "SDK not found"
**Rozwiązanie:**
```bash
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

### Problem: "Gradle build failed"
**Rozwiązanie:**
```bash
cd android
./gradlew clean
./gradlew build
```

### Problem: APK nie instaluje się
**Rozwiązanie:** Włącz "Nieznane źródła" w ustawieniach Android

---

## 📊 Rozmiar APK

- **PWA Builder:** ~5-10 MB
- **Capacitor:** ~8-15 MB
- **Bubblewrap:** ~3-7 MB (najmniejszy)

---

## 🎉 Publikacja w Google Play

1. **Stwórz konto:** https://play.google.com/console ($25 jednorazowo)

2. **Utwórz aplikację** → Wybierz nazwę "NumRun"

3. **Wypełnij dane:**
   - Kategoria: Edukacja / Gry
   - Typ: Gra
   - Opis: (skopiuj z manifest.json)

4. **Prześlij APK:**
   - Wersjonowanie: `versionCode: 1`, `versionName: "1.0.0"`
   - Prześlij podpisany APK

5. **Wypełnij kartę sklepu:**
   - Zrzuty ekranu (min. 2)
   - Ikona (512x512px)
   - Grafika prezentująca (1024x500px)

6. **Wyślij do weryfikacji** (2-7 dni)

---

## 📝 Checklist przed publikacją

- [ ] Przetestuj APK na urządzeniu
- [ ] Sprawdź czy wszystkie funkcje działają
- [ ] Zweryfikuj połączenie z Supabase
- [ ] Przetestuj na różnych wersjach Androida
- [ ] Sprawdź rozmiar APK (<15MB idealnie)
- [ ] Przygotuj politykę prywatności
- [ ] Przygotuj zrzuty ekranu (min. 4)
- [ ] Napisz opis aplikacji
- [ ] Ustaw wersjonowanie (versionCode, versionName)

---

## 🔗 Przydatne linki

- **PWA Builder:** https://www.pwabuilder.com/
- **Capacitor Docs:** https://capacitorjs.com/docs/android
- **Bubblewrap:** https://github.com/GoogleChromeLabs/bubblewrap
- **Android Developer:** https://developer.android.com/studio
- **Google Play Console:** https://play.google.com/console

---

## 💡 Wskazówki

1. **Testuj najpierw Debug APK** przed stworzeniem Release
2. **Przechowuj keystore w bezpiecznym miejscu** - strata = niemożność aktualizacji app
3. **Użyj PWA Builder** jeśli nie masz doświadczenia z Android Studio
4. **Capacitor** daje więcej kontroli i możliwości rozbudowy
5. **Bubblewrap** jest najlżejszy i najszybszy

---

Powodzenia! 🚀
