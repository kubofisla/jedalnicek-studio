from flask import (
    Blueprint, jsonify, request
)
from database.db_util import get_db
from database.schema import User, UserSettings, UserInventory, UserPlan
from sqlalchemy.orm import Session
from sqlalchemy import text

bp = Blueprint('user_data', __name__)

@bp.route('/api/user-data', methods=['GET', 'POST'])
def user_data():
    db = get_db()
    session = Session(db)
    
    # Simple auth mock - assume default user exists and we use it
    user = session.query(User).filter(User.sUsername == "default").first()
    if not user:
        # Fallback if default data not init, though it should be
        return jsonify({'error': 'Default user not found'}), 500
    
    user_id = user.nId

    if request.method == 'POST':
        data = request.get_json()
        if not data:
             return jsonify({'error': 'No data provided'}), 400

        # Settings
        if 'settings' in data:
            settings_data = data['settings']
            settings = session.query(UserSettings).filter(UserSettings.kUser == user_id).first()
            if not settings:
                settings = UserSettings(kUser=user_id)
                session.add(settings)
            
            settings.sStartDate = settings_data.get('startDate')
            settings.nDaysDuration = settings_data.get('daysDuration')
            settings.sLanguage = settings_data.get('language')

        # Inventory
        if 'inventory' in data:
            inventory_data = data['inventory']
            # Full replacement strategy for inventory as requested (or implied by simplified sync)
            # Or usually "sync". The prompt says "receive and persist this payload".
            # For simplicity let's clear existing inventory for user and re-add.
            session.query(UserInventory).filter(UserInventory.kUser == user_id).delete()
            
            for item in inventory_data:
                inv = UserInventory(
                    kUser=user_id,
                    sUid=item.get('uid'),
                    kRecipe=item.get('recipeId'),
                    nPortions=item.get('portions')
                )
                session.add(inv)

        # Plan
        if 'plan' in data:
            plan_data = data['plan']
            # Upsert strategy usually better for plan, but "receive and persist payload" might imply state.
            # However, plan is usually large. The request says "request will contain which month is requested... result will send all days in that month".
            # But for POST, it sends a payload.
            # Let's assume the payload contains the relevant plan items to save.
            # We can checks if items exist by UID.
            
            for item in plan_data:
                uid = item.get('uid')
                if not uid: continue
                
                plan_item = session.query(UserPlan).filter(UserPlan.kUser == user_id, UserPlan.sUid == uid).first()
                if not plan_item:
                    plan_item = UserPlan(kUser=user_id, sUid=uid)
                    session.add(plan_item)
                
                plan_item.sDate = item.get('date')
                plan_item.kRecipe = item.get('recipeId')
                plan_item.nPortions = item.get('portions')

        session.commit()
        return jsonify({'status': 'success'})

    elif request.method == 'GET':
        month = request.args.get('month') # YYYY-MM
        
        # Settings
        settings = session.query(UserSettings).filter(UserSettings.kUser == user_id).first()
        settings_dict = {}
        if settings:
            settings_dict = {
                'startDate': settings.sStartDate,
                'daysDuration': settings.nDaysDuration,
                'language': settings.sLanguage
            }

        # Inventory
        inventory_items = session.query(UserInventory).filter(UserInventory.kUser == user_id).all()
        inventory_list = []
        for item in inventory_items:
            inventory_list.append({
                'uid': item.sUid,
                'recipeId': item.kRecipe,
                'portions': item.nPortions
            })

        # Plan
        plan_query = session.query(UserPlan).filter(UserPlan.kUser == user_id)
        if month:
            # Filter by month string match or date range. Simple string match for YYYY-MM
            # Assuming sDate is YYYY-MM-DD
            plan_query = plan_query.filter(UserPlan.sDate.like(f"{month}%"))
        
        plan_items = plan_query.all()
        plan_list = []
        for item in plan_items:
            plan_list.append({
                'uid': item.sUid,
                'date': item.sDate,
                'recipeId': item.kRecipe,
                'portions': item.nPortions
            })

        response = jsonify({
            'settings': settings_dict,
            'inventory': inventory_list,
            'plan': plan_list
        })
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
