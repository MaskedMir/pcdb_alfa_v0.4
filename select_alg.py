from db_handler import *

cpu_procent = 0.25
gpu_procent = 0.40
motherboard_procent = 0.15
psd_procent = 0.06
ps_procent = 0.04
ram_procent = 0.05

power = 0


class select_alg(list):

    def select_cpu(self):  # Выбор CPU по параметам из уже отобранных по цене

        check = [0] * len(self)
        column = 2
        max_param = 0

        while column <= 4:
            for p in range(len(self)):
                if self[p][column] > max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        while column <= 6:
            max_param = 10 ** 9
            for p in range(len(self)):
                if self[p][column] < max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        return self[check.index(max(check))]

    def select_gpu(self):  # Выбор GPU по параметрам из уже отобранных по цене

        check = [0] * len(self)
        column = 2
        max_param = 0

        while column <= 3:
            for p in range(len(self)):
                if self[p][column] > max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        while column <= 5:
            max_param = 10 ** 9
            for p in range(len(self)):
                if self[p][column] < max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        return self[check.index(max(check))]

    def select_ram(self):  # Выбор RAM по параметрам из уже отобранных по цене

        check = [0] * len(self)
        column = 2
        max_param = 0

        while column <= 3:
            for p in range(len(self)):
                if self[p][column] > max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        while column <= 5:
            max_param = 10 ** 9
            for p in range(len(self)):
                if self[p][column] < max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        return self[check.index(max(check))]

    def select_psd(self):  # Выбор PSD по параметрам из уже отобранных по цене

        check = [0] * len(self)
        max_param = 0
        column = 2

        for p in range(len(self)):
            if self[p][column] > max_param:
                max_param = self[p][column]

        for cpu_n in range(len(self)):
            if max_param in self[cpu_n]:
                check[cpu_n] += 1
        column += 1

        while column <= 4:
            max_param = 10 ** 9
            for p in range(len(self)):
                if self[p][column] < max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        return self[check.index(max(check))]

    def select_mb(self):  # Выбор материнской платы по параметрам из уже отобранных по цене

        check = [0] * len(self)
        column = 2

        while column <= 3:
            max_param = 10 ** 9
            for p in range(len(self)):
                if self[p][column] < max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        return self[check.index(max(check))]

    def select_ps(self):  # Выбор блока питания по параметрам из уже отобранных по цене

        check = [0] * len(self)
        column = 2

        while column <= 3:
            max_param = 10 ** 9
            for p in range(len(self)):
                if self[p][column] < max_param:
                    max_param = self[p][column]

            for cpu_n in range(len(self)):
                if max_param in self[cpu_n]:
                    check[cpu_n] += 1
            column += 1

        return self[check.index(max(check))]


class db_search(float):  # Отбор из БД необходимых данных
    power = 0

    def search_cpu(price_pc):  # Отбор из БД CPU
        global power
        price_max = int(price_pc * (cpu_procent + 0.05))
        price_min = int(price_pc * (cpu_procent - 0.05))

        cpu_selection = db_sel("cpu", price_max, price_min)

        try:
            if len(cpu_selection) > 1:
                result = select_alg.select_cpu(cpu_selection)
            else:
                result = cpu_selection[0]
            power += result[5]
        except IndexError:
            result = ["Нет комплектующей", 0]

        return result

    def search_motherboard(cpu, price_pc):  # Отбор из БД материнской платы
        global power
        from db_handler import mb_db
        price_max = int(price_pc * (motherboard_procent + 0.05))
        price_min = int(price_pc * (motherboard_procent - 0.05))

        mb_sel = mb_db(cpu, price_max, price_min)

        try:
            if len(mb_sel) > 1:
                result = select_alg.select_mb(mb_sel)
            else:
                result = mb_sel[0]
            power += result[2]
        except IndexError:
            result = ["Нет комплектующей", 0]

        return result

    def search_gpu(price_pc):  # Отбор из БД GPU
        global power
        from db_handler import db_sel
        price_max = int(price_pc * (gpu_procent + 0.05))
        price_min = int(price_pc * (gpu_procent - 0.05))

        gpu_selection = db_sel("gpu", price_max, price_min)

        try:
            if len(gpu_selection) > 1:
                result = select_alg.select_gpu(gpu_selection)

            else:
                result = gpu_selection[0]
            power += result[4]
        except IndexError:
            result = ["Нет комплектующей", 0]

        return result

    def search_psd(price_pc):  # Отбор из БД PSD
        global power
        from db_handler import db_sel
        psd_price_max = int(price_pc * (psd_procent + 0.05))
        psd_price_min = int(price_pc * (psd_procent - 0.05))

        psd_selection = db_sel("psd", psd_price_max, psd_price_min)

        try:
            if len(psd_selection) > 1:
                result = select_alg.select_psd(psd_selection)
            else:
                result = psd_selection[0]
            power += result[3]
        except IndexError:
            result = ["Нет комплектующей", 0]

        return result

    def search_ram(price_pc):  # Отбор из БД RAM
        global power
        from db_handler import db_sel
        price_max = int(price_pc * (ram_procent + 0.05))
        price_min = int(price_pc * (ram_procent - 0.05))

        ram_selection = db_sel("ram", price_max, price_min)

        try:
            if len(ram_selection) > 1:
                result = select_alg.select_ram(ram_selection)
            else:
                result = ram_selection[0]
            power += result[4]
        except IndexError:
            result = ["Нет комплектующей", 0]

        return result

    def search_ps(price_pc):  # Отбор из БД блока питания
        global power
        from db_handler import ps_db
        price_max = int(price_pc * (ps_procent + 0.05))
        price_min = int(price_pc * (ps_procent - 0.05))

        ps_selection = ps_db(power, price_max, price_min)

        try:
            if len(ps_selection) > 1:
                result = select_alg.select_ps(ps_selection)
            else:
                result = ps_selection[0]
        except IndexError:
            result = ["Нет комплектующей", 0]

        return result


def pc_selection(price_pc):  # Сборка данных в один список (конечный список комплектующих для ПК)
    cpu = db_search.search_cpu(price_pc)
    motherboard = db_search.search_motherboard(cpu, price_pc)
    gpu = db_search.search_gpu(price_pc)
    ram = db_search.search_ram(price_pc)
    psd = db_search.search_psd(price_pc)
    ps = db_search.search_ps(price_pc)

    pc_list = [cpu, motherboard, gpu, ram, psd, ps]
    return pc_list
