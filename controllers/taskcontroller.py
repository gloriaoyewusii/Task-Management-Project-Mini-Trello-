
import os

from flask import request, make_response, jsonify

from src.dtos.request.createboardrequest import CreateBoardRequest
from src.dtos.request.taskcreationrequest import CreateTaskRequest
from src.dtos.request.updatetaskrequest import UpdateTaskRequest
from src.dtos.response.taskcreationresponse import TaskCreationResponse

from src.exceptions.board_not_found_error import BoardNotFoundError
from src.exceptions.boardcreationerror import BoardCreationError

from src.exceptions.existingboarderror import ExistingBoardError
from src.exceptions.existingtaskerror import ExistingTaskError
from src.exceptions.task_not_found_error import TaskNotFoundError
from src.exceptions.taskcreationfailederror import TaskCreationFailedError
from src.exceptions.user_not_found_error import UserNotFoundError

from src.models.board import Board
from src.models.task import Task
from src.repositories.board_repository import BoardRepository
from src.repositories.task_repository import TaskRepository

from src.services.boardservice import BoardService

from dotenv import load_dotenv

from src.services.taskservice import TaskService

load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')


class TaskController:
    def __init__(self, task_service : TaskService):
        self.task_service = task_service

    @staticmethod
    def create_task():
        task_data = request.get_json()
        title = task_data.get('title')
        description = task_data.get('description')
        task_status = task_data.get('task_status')
        board = task_data.get('board')
        assigned_to = task_data.get('assigned_to')
        due_date = task_data.get('due_date')

        if TaskRepository.get_task_by_title(title):
            return jsonify({'error': 'Task with this title already exists'}), 409

        try:
            TaskService.create_task(title, description, task_status, board, assigned_to, due_date)
            task = Task.objects.get(board=board).first()

            task_creation_request = CreateTaskRequest()
            serialised_task = task_creation_request.dump(task)
            return make_response(jsonify({
                "message": "Task added successfully",
                "board": serialised_task}), 201)

        except TaskCreationFailedError as e:
            return make_response(jsonify({"error": str(e)}), 401)
        except ExistingTaskError as e:
            return make_response(jsonify({"error": str(e)}), 401)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 401)

    @staticmethod
    def view_task(task_id):
        # task_data = request.get_json()
        #
        # task_id = task_data.get('task_id')
        if not task_id:
            return make_response(jsonify({'message': 'Task owner ID is required'}), 400)
        try:
            task_details = TaskService.view_task(task_id)
            return task_details
        except TaskNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


    @staticmethod
    def delete_task(task_id):
        # task_data = request.get_json()
        # task_id = task_data.get('board_id')
        if not task_id:
            return make_response(jsonify({"error": "Task ID is required"}), 400)

        try:
            deletion_message = TaskService.delete_task(task_id)
            return make_response(jsonify({"message":deletion_message}), 200)
        except TaskNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

    @staticmethod
    def update_task(task_id):
        try:
            task_data = request.get_json()
            update_schema = UpdateTaskRequest()
            validated_update = update_schema.load(task_data)
            updated_task = TaskService.update_task(task_id, validated_update)
            return make_response(jsonify({
                "message": "Task updated successfully",
                "data": updated_task.to_dict()
            }), 200)
        except TaskNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except UserNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 404)
        except TaskCreationFailedError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)









