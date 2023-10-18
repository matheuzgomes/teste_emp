class Store:
    def __init__(self, motoboy):
        self.motoboy: str = motoboy
        self.validate()
        self.store_1 = [50, 50, 50]
        self.store_2 = [50, 50, 50, 50]
        self.store_3 = [50, 50, 100]

    def execute(self) -> float:
        result = []
        if "4" not in self.motoboy:
            for i in self.store_1:
                percentage = (i * 5) / 100.0
                percentage += 2 if "5" not in self.motoboy else 3
                result.append(percentage)
            for i in self.store_2:
                percentage = (i * 5) / 100.0
                percentage += 2 if "5" not in self.motoboy else 3
                result.append(percentage)
            for i in self.store_3:
                percentage = (i * 15) / 100.0
                percentage += 2 if "5" not in self.motoboy else 3
                result.append(percentage)
        else:
            if "4" in self.motoboy:
                for i in self.store_1:
                    percentage = (i * 5) / 100.0
                    percentage += 2
                    result.append(percentage)
            
        return f"O {self.motoboy} vai ganhar um total de R${sum(result)} trabalhando para as lojas {'1, 2, 3' if '4' not in self.motoboy else '1'}"
    

    def validate(self):
        if not isinstance(self.motoboy, str):
            raise ValueError("Motoboy name must be an string")
        if not self.motoboy.startswith(('Moto', 'moto')):
            raise ValueError ("Not a valid motoboy name")
        list_ = list(self.motoboy.strip())
        if int(list_[-1]) >= 6:
            raise ValueError("Motoboy not registered")
        

if __name__ == "__main__":
    motoboy = input("Por favor digite o motoboy desejado: \n")


    teste = Store(motoboy).execute()

    print(teste)
