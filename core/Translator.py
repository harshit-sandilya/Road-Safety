import argostranslate.package as package
import argostranslate.translate as translate


class Translator:
    def __init__(self):
        self.download_models("en", "hi")
        self.download_models("hi", "en")

    def download_models(self, from_code, to_code):
        package.update_package_index()
        available_packages = package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code,
                available_packages,
            )
        )
        package.install_from_path(package_to_install.download())

    def translate_en(self, text):
        return translate.translate(text, "en", "hi")

    def translate_hi(self, text):
        return translate.translate(text, "hi", "en")
