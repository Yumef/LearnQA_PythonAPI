import pytest
import requests
import json

class TestUserAgentCheck:
    data = [
        (
            "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mobile",
            "No",
            "Android"
        ),
        (
            "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "Mobile",
            "Chrome",
            "iOS"
        ),
        (
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Googlebot",
            "Unknown",
            "Unknown"
        ),
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "Web",
            "Chrome",
            "No"
        ),
        (
            "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "Mobile",
            "No",
            "iPhone"
        )
    ]

    @pytest.mark.parametrize('user_agent, platform, browser, device', data)
    def test_user_agent_check_platform(self, user_agent, platform, browser, device):
        agent = {"User-Agent": user_agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=agent)
        response2 = response.json()
        assert response2.get("platform") == platform, "Platform is not expected"

    @pytest.mark.parametrize('user_agent, platform, browser, device', data)
    def test_user_agent_check_browser(self, user_agent, platform, browser, device):
        agent = {"User-Agent": user_agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=agent)
        response2 = response.json()
        assert response2.get("browser") == browser, "Browser is not expected"

    @pytest.mark.parametrize('user_agent, platform, browser, device', data)
    def test_user_agent_check_device(self, user_agent, platform, browser, device):
        agent = {"User-Agent": user_agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=agent)
        response2 = response.json()
        assert response2.get("device") == device, "Device is not expected"

