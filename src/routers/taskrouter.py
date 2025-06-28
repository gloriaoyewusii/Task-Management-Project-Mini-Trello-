
from flask import Blueprint

from controllers.taskcontroller import TaskController

from src.services.taskservice import TaskService

task_router = Blueprint('task_router', __name__)
task_service = TaskService()
task_controller = TaskController(task_service)

@task_router.route('/task', methods=['POST'])
def create_task():
    return task_controller.create_task()

@task_router.route('/task/<task_id>', methods=['GET'])
def view_task(task_id):
    return task_controller.view_task(task_id)

@task_router.route('/task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    return task_controller.delete_task(task_id)
@task_router.route('/task/<task_id>', methods=['PUT'])
def update_task(task_id):
    return task_controller.update_task(task_id)