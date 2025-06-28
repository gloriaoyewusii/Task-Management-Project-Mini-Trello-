
from flask import Blueprint

from controllers.boardcontroller import BoardController
from src.services.boardservice import BoardService

board_router = Blueprint('board_router', __name__)
board_service = BoardService()
board_controller = BoardController(board_service)

@board_router.route('/board', methods=['POST'])
def create_board():
    return board_controller.create_board()

@board_router.route('/board/<board_id>', methods=['GET'])
def view_board(board_id):
    return board_controller.view_board(board_id)

@board_router.route('/board/<board_id>', methods=['DELETE'])
def delete_board(board_id):
    return board_controller.delete_board(board_id)