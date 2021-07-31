import pytest
import requests
import json

class TestUserAgentCheck:
    user_agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('value', user_agents)
    def test_user_agent_check(self, value):
        if value == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": value})
            response2 = response.json()
            assert response2.get("platform") == "Mobile", "Platform is not 'Mobile'"
            assert response2.get("browser") == "No", "Browser is not 'No'"
            assert response2.get("device") == "Android", "Device is not 'Android'"

        if value == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": value})
            response2 = response.json()
            assert response2.get("platform") == "Mobile", "Platform is not 'Mobile'"
            assert response2.get("browser") == "Chrome", "Browser is not 'Chrome'"
            assert response2.get("device") == "iOS", "Device is not 'iOS'"

        if value == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": value})
            response2 = response.json()
            assert response2.get("platform") == "Googlebot", "Platform is not 'Googlebot'"
            assert response2.get("browser") == "Unknown", "Browser is not 'Unknown'"
            assert response2.get("device") == "Unknown", "Device is not 'Unknown'"

        if value == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": value})
            response2 = response.json()
            assert response2.get("platform") == "Web", "Platform is not 'Web'"
            assert response2.get("browser") == "Chrome", "Browser is not 'Chrome'"
            assert response2.get("device") == "No", "Device is not 'No'"

        if value == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
            response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": value})
            response2 = response.json()
            assert response2.get("platform") == "Mobile", "Platform is not 'Mobile'"
            assert response2.get("browser") == "No", "Browser is not 'No'"
            assert response2.get("device") == "iPhone", "Device is not 'iPhone'"
