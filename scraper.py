import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_portfolio():
    # URL вашего сайта
    url = "https://trh-dt.github.io/portfolio_DT/index.html"
    
    try:
        # Отправляем GET-запрос
        response = requests.get(url)
        response.raise_for_status()  # Проверяем на ошибки
        
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Собираем данные
        portfolio_data = {
            "title": soup.title.string if soup.title else "No title",
            "description": soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else "No description",
            "projects": [],
            "skills": [],
            "contacts": {}
        }
        
        # Собираем проекты
        project_sections = soup.find_all('section', class_='card')
        for section in project_sections:
            if section.find('h3') and section.find('h3').text == "Projects":
                projects = section.find_all('li')
                for project in projects:
                    portfolio_data["projects"].append(project.text.strip())
        
        # Собираем навыки
        skills_section = soup.find('section', class_='card')
        if skills_section and skills_section.find('h3') and skills_section.find('h3').text == "Skills":
            skills = skills_section.find_all('li')
            for skill in skills:
                portfolio_data["skills"].append(skill.text.strip())
        
        # Собираем контакты
        contacts_section = soup.find('section', class_='contacts-card')
        if contacts_section:
            contacts = contacts_section.find_all('li')
            for contact in contacts:
                text = contact.text.strip()
                if 'Email:' in text:
                    portfolio_data["contacts"]["email"] = text.split('Email:')[1].strip()
                elif 'Telegram:' in text:
                    portfolio_data["contacts"]["telegram"] = text.split('Telegram:')[1].strip()
                elif 'GitHub:' in text:
                    portfolio_data["contacts"]["github"] = text.split('GitHub:')[1].strip()
        
        # Сохраняем данные в JSON файл
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_data_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(portfolio_data, f, ensure_ascii=False, indent=4)
        
        print(f"Данные успешно сохранены в файл {filename}")
        return portfolio_data
        
    except requests.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
        return None

if __name__ == "__main__":
    data = scrape_portfolio()
    if data:
        print("\nСобранные данные:")
        print(json.dumps(data, ensure_ascii=False, indent=2)) 