from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from ballapp3.session import forms
from ballapp3.session.data import SessionManager
from ballapp3.session.stats import StatsManager
import datetime


session = Blueprint('session', __name__)


# Context Processors:
@session.context_processor
def session_processor():
    '''
    This Context Processor give the ability to access all
        the kinds of sessions via url
    :param session_type:
    :return:
    '''
    # The session type should be brought from the current url
    current_session_type = request.view_args.get('session_type')
    if current_session_type:
        mngr = SessionManager(current_session_type)
        return dict(sessions=mngr.get_json_files(remove_extension=True), session_type=current_session_type)
    else:
        return {}

# TODO: DELETE AFTER APP DEV IS FINISHED DEVELOPING:
@session.route("/")
def redirect_to_favorite_location():
    return redirect(
        url_for(
            "session.edit_session_route",
            session_type='free_throw',
            session_name='15_09_21_13_15_00'
        )
    )

@session.route('/attempts_str/<session_type>/<session_name>', methods=["GET"])
def attempts_str_json(session_type, session_name):
    mngr = SessionManager(session_type)
    data = mngr.get_content(session_name)
    return jsonify({
        'attempts_str' : data.get('session').get('attempts_str')
    })


@session.route("/session/<session_type>/<session_name>", methods=["GET","POST"])
def edit_session_route(session_type, session_name):
    mngr = SessionManager(session_type)
    try:
        data = mngr.get_content(session_name)
        attempts_str = data.get('session').get('attempts_str')
        stats_manager = StatsManager(attempts_str)
        stats = stats_manager.all_stats()
        return render_template(
            'edit_session.html',
            session_type=session_type,
            session_name=session_name,
            made_control_btn_values=[5, 1, -1],
            missed_control_btn_values=[1, -1],
            attempts_str=attempts_str,
            stats=stats
        )
    except FileNotFoundError:
        if request.method == 'GET':
            continue_form = forms.ContinueSessionCreationForm()
            # Do something else if the json file is not found:
            flash(
                "Session does not exist, would you like to start new ?",
                category='warning'
            )

            return render_template(
                "ensure_session_create.html",
                continue_form=continue_form,
            )
        if request.method == 'POST':
            now = datetime.datetime.now()
            # Format the datetime with the convention we want
            new_session_name = f"{now:%d_%m_%y_%H_%M_%S}"
            # Create a JSON file for that session
            mngr.create_file(new_session_name)
            return redirect(
                url_for(
                    'session.edit_session_route',
                    session_type='free_throw',
                    session_name=new_session_name
                )
            )


@session.route("/session_update_json/<session_type>/<session_name>", methods=["POST"])
def update_data_json(session_type, session_name):
    if request.method == 'POST':
        mngr = SessionManager(session_type)
        value = request.form.get('value')
        attempt_result = '1' if 'made' in request.form.get('attempt_result') else '0'
        if int(value) > 0:
            mngr.edit_file_attempts_str(
                name=f"{session_name}.json",
                attempts_str=attempt_result * int(value)
            )
        else:
            mngr.edit_file_attempts_str(
                name=f"{session_name}.json",
                attempts_str='',
                delete_last=True
            )
        return ('', 204)