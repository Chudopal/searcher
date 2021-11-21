from programm import Programm


database = "app/db.db"
migration = "app/migrations.sql"


def main(database: str, migration: str):
    programm = Programm(
        database=database,
        migration=migration
    )
    programm.process()


if __name__ == "__main__":
    main(
        database=database,
        migration=migration
    )
