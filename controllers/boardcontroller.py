
import os

from flask import request, make_response, jsonify
from marshmallow import ValidationError

from src.dtos.request.createboardrequest import CreateBoardRequest
from src.dtos.response.boardcreationresponse import CreateBoardResponse

from src.exceptions.board_not_found_error import BoardNotFoundError
from src.exceptions.boardcreationerror import BoardCreationError

from src.exceptions.existingboarderror import ExistingBoardError

from src.models.board import Board
from src.repositories.board_repository import BoardRepository

from src.services.boardservice import BoardService

from dotenv import load_dotenv

# load_dotenv()
# SECRET_KEY = os.environ.get('SECRET_KEY')


class BoardController:
    def __init__(self, board_service : BoardService):
        self.board_service = board_service

    @staticmethod
    def create_board():
        try:
            board_schema = CreateBoardRequest()
            board_data = request.get_json()
            validated_board = board_schema.load(board_data)
        except ValidationError as err:
            return make_response(jsonify({'error': err.messages}), 400)

        title = validated_board.get('title')
        description = validated_board.get('description')
        owner = validated_board.get('owner')
        board_members = validated_board.get('board_members')

        existing_board = BoardRepository.get_board_by_owner(owner)
        if existing_board:
            return jsonify({'message': 'Board already exists'}), 409

        try:
            created_board = BoardService.create_board(title, description, owner, board_members)

            board_creation_response = CreateBoardResponse()
            serialised_board = board_creation_response.dump(created_board)
            return make_response(jsonify({
                "message": "Board created successfully",
                "board": serialised_board}), 201)

        except BoardCreationError as e:
            return make_response(jsonify({"error": str(e)}), 401)
        except ExistingBoardError as e:
            return make_response(jsonify({"error": str(e)}), 401)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 401)

    @staticmethod
    def view_board(board_id):
        # board_data = request.get_json()
        #
        # board_owner = board_data.get('owner')
        if not board_id:
            return make_response(jsonify({'message': 'Board owner ID is required'}), 400)
        try:
            board_details = BoardService.view_board(board_id)
            return make_response(jsonify({
                "message": "Board retrieved successfully",
                "board": board_details
            }), 200)

        except BoardNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


    @staticmethod
    def delete_board(board_id):
        # board_data = request.get_json()
        # board_id = board_data.get('board_id')
        if not board_id:
            return make_response(jsonify({"error": "Board identification is required"}), 400)

        try:
            deletion_message = BoardService.delete_board(board_id)
            return make_response(jsonify({"message":deletion_message}), 200)
        except BoardNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)






