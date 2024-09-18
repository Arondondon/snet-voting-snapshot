from sqlalchemy.exc import SQLAlchemyError

from snapshot.infrastructure.repository.base_repository import BaseRepository
from snapshot.infrastructure.model import Balances


class BalanceSnapshotRepository(BaseRepository):
    def add_user_balance(self, network, address, balance, stake=0, stake_key=None):

        user_balance = self.get_user_balance(network, address)
        if user_balance:
            user_balance.balance += balance
            user_balance.stake += stake
            if stake_key:
                user_balance.stake_key = stake_key
        else:
            if not stake_key:
                user_balance = Balances(network=network,
                                        address=address,
                                        balance=balance,
                                        stake=stake)
            else:
                user_balance = Balances(network=network,
                                        address=address,
                                        balance=balance,
                                        stake=stake,
                                        stake_key=stake_key)
        try:
            self.session.add(user_balance)
            self.session.commit()
            return user_balance
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_user_balance(self, network, address):
        return self.session.query(Balances).filter_by(network=network, address=address).first()
