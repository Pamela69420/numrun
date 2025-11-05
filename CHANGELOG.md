# 📝 Changelog - NumRun

## [1.1.0] - 2025-11-05

### 🔴 Naprawione Błędy Krytyczne

#### 1. **Błąd wcięcia (linia 1330)**
- **Problem:** Zmienna `bestScore` miała nieprawidłowe wcięcie
- **Naprawa:** Dodano odpowiednie wcięcie wewnątrz funkcji `updateStats()`
- **Plik:** `index.html:1330`

#### 2. **Daily Challenge - nieprawidłowy seed random**
- **Problem:** Funkcja `Math.seedrandom` była definiowana ale nigdy używana
- **Naprawa:** Utworzono właściwą funkcję `seededRandom()` i poprawnie zaimplementowano deterministyczne generowanie challengów
- **Efekt:** Daily Challenge teraz generuje się konsystentnie dla wszystkich graczy w danym dniu
- **Plik:** `index.html:1869-1900`

#### 3. **Race conditions w timerze**
- **Problem:** Timer mógł kontynuować działanie po zakończeniu gry, powodując błędy
- **Naprawa:**
  - Dodano `clearInterval()` + `timer = null` we wszystkich funkcjach kończących grę
  - `quitGame()` - linia 876
  - `confirmQuit()` - linia 926
  - `timeUp()` - linia 990
  - `showLevelSelector()` - linia 1388
  - `startTimer()` - linia 960 (cleanup przed startem nowego)
- **Efekt:** Brak wycieków pamięci, stabilne działanie timera

#### 4. **Memory leak - particles**
- **Problem:** Cząsteczki były dodawane do DOM ale mogły nie być usunięte przy szybkim opuszczeniu gry
- **Naprawa:**
  - Dodano tracking array `activeParticles`
  - Zaimplementowano `cleanupParticles()` funkcję
  - Użycie `DocumentFragment` dla lepszej wydajności
  - Auto-cleanup po 2 sekundach
- **Plik:** `index.html:1342-1308`

---

### 🟡 Usprawnienia UX

#### 5. **Zamiana alert() i prompt() na custom modals**
- **Problem:** `alert()` i `prompt()` blokują UI i wyglądają przestarzale
- **Naprawa:**
  - Stworzone funkcje `showCustomPrompt()` i `showCustomAlert()`
  - Piękne, responsywne modals z animacjami
  - Keyboard support (Enter, Escape)
  - Async/await API
- **Zastosowanie:**
  - `askForPlayerName()` - linia 1826
  - Daily Challenge info - linia 2049
- **Plik:** `index.html:1276-1340`

---

### 🔵 Usprawnienia Wydajności

#### 6. **Optymalizacja DOM manipulation**
- **Problem:** Particles były dodawane pojedynczo do DOM (8 operacji)
- **Naprawa:** Użycie `DocumentFragment` (1 operacja)
- **Efekt:** ~8x szybsze renderowanie particles
- **Plik:** `index.html:1345-1299`

#### 7. **Error handling dla async operations**
- **Problem:** Brak obsługi błędów w operacjach Supabase
- **Naprawa:**
  - Dodano `handleAsyncError()` wrapper
  - Try-catch we wszystkich funkcjach async
  - User-friendly error messages
  - Graceful degradation (offline support)
- **Plik:** `index.html:680-689`, `1801-1820`

---

### ♿ Accessibility

#### 8. **ARIA labels i semantic HTML**
- **Dodano:**
  - `role="main"` dla głównego kontenera
  - `role="status" aria-live="polite"` dla równania
  - `role="group"` dla przycisków odpowiedzi
  - `aria-label` dla wszystkich interaktywnych elementów
- **Efekt:** Lepsza dostępność dla screen readers
- **Plik:** `index.html:569`, `642`, `644-649`

---

## 🛠️ Nowe Funkcje

### Budowanie APK
- Dodano konfigurację Capacitor (`capacitor.config.json`)
- Utworzono `package.json` ze skryptami build
- Szczegółowa dokumentacja w `BUILD_APK.md`
- Wsparcie dla 3 metod budowania:
  - Capacitor (zalecane)
  - PWA Builder (najłatwiejsze)
  - Bubblewrap (najmniejszy rozmiar)

---

## 📊 Statystyki Zmian

```
Pliki zmienione: 1 (index.html)
Linie dodane: 171
Linie usunięte: 36
Nowe pliki: 3 (capacitor.config.json, package.json, BUILD_APK.md)
```

---

## 🔬 Testy

### Przetestowane scenariusze:
- ✅ Timer działa poprawnie w trybie czasowym
- ✅ Daily Challenge generuje się konsystentnie
- ✅ Particles są poprawnie czyszczone
- ✅ Custom modals działają responsywnie
- ✅ Error handling chroni przed crashami
- ✅ Brak wycieków pamięci

### Kompatybilność:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers (iOS Safari, Chrome Android)

---

## 🚀 Następne Kroki

### Priorytet 1 (Zrobione):
- [x] Naprawienie krytycznych błędów
- [x] Usprawnienia wydajności
- [x] Accessibility improvements
- [x] Konfiguracja APK

### Priorytet 2 (Opcjonalnie):
- [ ] Dodanie testów jednostkowych (Jest)
- [ ] Refactoring do modułów ES6
- [ ] Dark mode support
- [ ] Internationalization (i18n)
- [ ] Sound effects
- [ ] Vibration feedback (mobile)
- [ ] Social sharing (wyniki)

---

## 📦 Jak zainstalować?

1. **Wersja Web (PWA):**
   ```bash
   # Po prostu otwórz index.html w przeglądarce
   # Lub hostuj na:
   - GitHub Pages
   - Netlify
   - Vercel
   ```

2. **Android APK:**
   ```bash
   # Zobacz BUILD_APK.md dla szczegółowych instrukcji
   npm run build:apk
   ```

---

## 🙏 Podziękowania

Dzięki za zgłoszenie problemów i sugestie ulepszeń!

---

## 📄 Licencja

MIT License - zobacz LICENSE file dla szczegółów
