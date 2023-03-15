import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class Global2():

    def __init__(self, driver):
        self.driver = driver

    def Saludo(self):
        print("Hola Papu")

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url, tie):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Se muestra l apagina: []" + Url)
        t = time.sleep(tie)
        return t

    def Texto_xpath_try(self, xpath, texto, tie):
        try:
            var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
            var = self.driver.find_element(By.XPATH, value=xpath)
            var.clear()
            var.send_keys(texto)
            print("Escribiendo en el campo {} el texto {} ->".format(xpath, texto))
            t = time.sleep(tie)
            return t
        except TimeoutException as ex:
            print("ex.msg")
            print("No se encontro el elemento" + xpath)

    def Texto_ID_try(self, id, texto, tie):
        try:
            var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, id)))
            var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
            var = self.driver.find_element(By.XPATH, value=id)
            var.clear()
            var.send_keys(texto)
            print("Escribiendo en el campo {} el texto {} ->".format(id, texto))
            t = time.sleep(tie)
            return t
        except TimeoutException as ex:
            print("ex.msg")
            print("No se encontro el elemento" + id)

    def Click_ID(self, id, tie):
        try:
            var = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, id)))
            var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
            var = self.driver.find_element(By.ID, value=id)
            var.click()
            print("Damos click en el campo {}".format(id))
            t = time.sleep(tie)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + id)

    def Click_xpath(self, xpath, tie):
        try:
            var = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, xpath)))
            var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
            var = self.driver.find_element(By.ID, value=xpath)
            var.click()
            print("Damos click en el campo {}".format(id))
            t = time.sleep(tie)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)

    def Select_xpath(self, xpath, texto, tie):
        try:
            var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
            var = self.driver.find_element(By.XPATH, value=xpath)
            var = Select(var)
            var.select_by_visible_text(texto)
            print("El campo seleccionado es -> {}".format(texto))
            t = time.sleep(tie)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)

    def Select_xpath_type(self, xpath, tipo, dato, tie):
        try:
            var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
            var = self.driver.find_element(By.XPATH, value=xpath)
            var = Select(var)
            if tipo == "text":
                var.select_by_visible_text(dato)
            elif tipo == "index":
                var.select_by_index(dato)
            elif tipo == "value":
                var.deselect_by_value(dato)
            print("El campo seleccionado es -> {}".format(dato))
            t = time.sleep(tie)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento" + xpath)

    def Check_xpath_multiples(self, tie, *args):
        try:
            for num in args:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, num)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.XPATH, value=num)
                var.click()
                print("Damos click en el campo {}".format(num))
                t = time.sleep(tie)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el elemento" + num)

    def Texto_Mixto(self, tipo, selector, texto, tie):
        if tipo == "xpath":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.XPATH, value=selector)
                var.clear()
                var.send_keys(texto)
                print("Escribiendo en el campo {} el texto {} ->".format(selector, texto))
                t = time.sleep(tie)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encontro el elemento" + selector)
        elif tipo == "ID":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.XPATH, value=selector)
                var.clear()
                var.send_keys(texto)
                print("Escribiendo en el campo {} en texto {} ->".format(selector, texto))
                t = time.sleep(tie)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)

    def Click_Mixto(self, tipo, selector, tie):
        if tipo == "xpath":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.XPATH, value=selector)
                var.click()
                print("Damos click en el campo {}".format(selector))
                t = time.sleep(tie)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("no se encontro el elemento" + selector)
        elif tipo == "ID":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.ID, value=selector)
                var.click()
                print("Damos click en el campo {}".format(selector))
                t = time.sleep(tie)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)

    def Existe(self, tipo, selector, tie):
        if tipo == "xpath":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.ID, value=selector)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("NO se encontro el elemento" + selector)
                return "No existe"
        elif tipo == "ID":
            try:
                var = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, selector)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.ID, value=selector)
                print("El elemento {} -> existe".format(selector))
                t = time.sleep(tie)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento" + selector)
                return "No existe"

    def Cierre(self):
        print("la prueba finaliza correctamente")

