
from webdriver_manager.core import driver

from Practice.pageObjects.CheckoutPage import CheckoutPage
from Practice.pageObjects.HomePage import HomePage
from Practice.utils.BaseClass import BaseClass


class EcomerceTest(BaseClass):
    def test_e2e(self):
        cardText = ""
        homePage = HomePage(self.driver)
        homePage.shopItems
        checkoutPage = CheckoutPage(self.driver)
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.Text
            print(cardText)
        if cardText == "Blackberry":
            checkoutPage.getCardFooter()[i]
        checkoutPage.getCheckoutButton
        checkoutPage.getCheckoutPage
        
