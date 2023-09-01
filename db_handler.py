import sqlite3


def mb_db(cpu, price_max, price_min):
    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM motherboard '
                f'WHERE (price <= {price_max})'
                f'AND (price >=  {price_min})'
                f'AND ((SELECT cpu.chipset FROM cpu WHERE cpu.name = "{cpu[0]}") = motherboard.chipset)')
    selection = cur.fetchall()

    return selection


def ps_db(power, price_max, price_min):
    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM ps '
                f'WHERE (price <= {price_max})'
                f'AND (price >=  {price_min})'
                f'AND (power >= {power})')
    selection = cur.fetchall()

    return selection


def db_sel(table, price_max, price_min):
    con = sqlite3.connect('pcdb.db')
    cur = con.cursor()
    selection = None
    if table == "cpu":
        cur.execute(f'SELECT * FROM cpu '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "gpu":
        cur.execute(f'SELECT * FROM gpu '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "psd":
        cur.execute(f'SELECT * FROM psd '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    if table == "ram":
        cur.execute(f'SELECT * FROM ram '
                    f'WHERE (price <= {price_max})'
                    f'AND (price >=  {price_min})')
        selection = cur.fetchall()

    return selection


def db_pc_list(pcl):
    price = pcl[0][-1] + pcl[1][-1] + pcl[2][-1] + pcl[3][-1] + pcl[4][-1] + pcl[5][-1]
    con = sqlite3.connect("pcdb.db")
    cur = con.cursor()
    cur.execute(f'INSERT INTO pc '
                f'(cpu, gpu, motherboard, psd, ram, ps, price)'
                f'VALUES ("{pcl[0][0]}", "{pcl[1][0]}", "{pcl[2][0]}", "{pcl[3][0]}",'
                f'"{pcl[4][0]}", "{pcl[5][0]}", "{price}")')
    con.commit()

    return price