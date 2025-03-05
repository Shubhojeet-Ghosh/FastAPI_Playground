from models.user_models.user import *

def listen_user_controller(session_data):
    try:
        session_id = session_data.session_id
        print(f"User Captured with session id : {session_id}")

        return ResponseFormat(
            success=True,
            message=f"User acknowledged with session id: {session_id}"
        )
    
    except Exception as e:
        print(f"Error in listen_user : {e}")
        return ResponseFormat(
            success=False,
            message=f"Error in listen_user : {str(e)}"
        )