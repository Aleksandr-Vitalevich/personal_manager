#!/bin/bash
# Автоматически определяем текущую папку проекта (работает и на флешке)
cd "$(dirname "$0")"

# === БЛОК АВТОМАТИЧЕСКОЙ НАСТРОЙКИ ОКРУЖЕНИЯ ===
# Проверяем, существует ли папка .venv
if [ ! -d ".venv" ]; then
    echo "📦 Первичный запуск: создание виртуального окружения..."
    
    # 1. Создаем чистое окружение
    python3 -m venv .venv
    
    # 2. Активируем его для установки зависимостей
    source .venv/bin/activate
    
    # 3. Обновляем pip на всякий случай
    pip install --upgrade pip
    
    # 4. Проверяем, есть ли файл со списком библиотек, и устанавливаем их
    if [ -f "requirements.txt" ]; then
        echo "📥 Установка необходимых библиотек из requirements.txt..."
        pip install -r requirements.txt
        echo "✅ Все библиотеки успешно установлены!"
    else
        echo "⚠️ Внимание: файл requirements.txt не найден! Установите зависимости вручную."
    fi
else
    # Если папка .venv уже есть — просто активируем её
    source .venv/bin/activate
fi
# ===============================================

# Запускаем Streamlit в фоне на безопасном порту 8080
streamlit run main_operation.py --server.headless true --server.port 8080 &

# Даем серверу 1.5 секунды подняться
sleep 1.5

URL="http://localhost:8080"

# Наша неубиваемая cross-platform логика проверки браузеров
if [[ "$OSTYPE" == "darwin"* ]]; then
    if open -Ra "Google Chrome" 2>/dev/null; then
        open -a "Google Chrome" --args --app="$URL"
    elif open -Ra "Yandex" 2>/dev/null; then
        open -a "Yandex" --args --app="$URL"
    else
        echo "💡 Для запуска в виде отдельного окна без рамок установите Google Chrome."
        open -a "Safari" "$URL"
    fi
else
    if command -v google-chrome &> /dev/null; then
        google-chrome --app="$URL"
    elif command -v yandex-browser &> /dev/null; then
        yandex-browser --app="$URL"
    elif command -v firefox &> /dev/null; then
        echo "💡 Для запуска в виде отдельного окна без рамок установите Google Chrome."
        firefox "$URL"
    else
        xdg-open "$URL"
    fi
fi
