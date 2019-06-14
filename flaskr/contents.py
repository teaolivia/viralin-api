#!flask/bin/python
from flask import Flask, jsonify, request, abort, make_response, url_for
from flaskr import apis, login, db, dynamo
from models import models
import json
import requests

class Contents(object):
    def __init__(self, id):
        self.content_id = id

    @apis.route('/<seller_id>/contents', methods=['POST'])
    def add_content(self, sellerId):
        if not request.json or not 'username' in request.json:
            abort(400)
        title = request.form.get('title',None)
        content_type = request.form.get('content_type',None)
        duration = request.form.get('duration',None)
        form = request.form.get('type',None)
        asset = request.form.get('asset',None)            
        rule = request.form.get('game_rule',None)
        content = {
            'seller_id': request.json['seller_id'],
            '_id': _id[-1]['_id'] + 1,
            'title': request.json['title'],
            'status': True,
            'isReferral': True,
            'content_type': request.json['content_type'],
            'duration': request.json['duration'],
            'type': request.json['form'],
            'asset': request.json['asset'],
            'games_rule': request.json.get('rule', "")
        }
        dynamo.tables['contents'].put_item(content)
        
    @apis.route('/<seller_id>/contents', methods=['DELETE'])
    def delete_content(self, seller_id, content_id, promo_id):
        db.Contents.deleteOne( { "seller_id": seller_id, "_id": content_id } )
        # delete in dynamoDB
        contents.delete_item(Key = {'content_id': content_id})
        contentpromo.delete_item(Key = {'content_id': content_id, 'promo_id': promo_id})
        return jsonify({'result': True})

    @apis.route('/<seller_id>/contents', methods=['PUT'])
    def edit_content(self, username):
        pass

    @apis.route('/<seller_id>/contents', methods=['PUT'])
    def toggle_active_content(self, username, content_id, stat):
        if stat == True:
            stat = False
        else:
            stat = True

    @apis.route('/contents/duration/', methods=['POST'])
    def set_duration(self, username, content_id, start, end) -> int:
        self.duration_start = start
        self.duration_end = end
        return self.duration_end - self.duration_start

    @apis.route('/contents/<content_id>/share', methods=['POST'])
    def share_link(self, content_id) -> str:
        return url_for('/<seller_id>/<content_id>')

    @apis.route('/contents/<content_id>/<promotor_id>', methods=['POST'])
    def respond_request(self, content_id, promotor_id):
        pass
    
# # main driver
# if __name__ == '__main__':
#     app.run(port=5003,debug=True)