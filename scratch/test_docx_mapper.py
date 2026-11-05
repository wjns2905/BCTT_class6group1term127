import sys, os, docx, json, re

sys.stdout.reconfigure(encoding='utf-8')

docx_configs = [
    {
        'doc_name': '[BCTT] Trending.docx',
        'cat_folder': 'trending',
        'articles': [
            {'num': '1', 'target_id': 'trending-1'},
            {'num': '2', 'target_id': 'trending-2'},
            {'num': '3', 'target_id': 'trending-3'},
            {'num': '4', 'target_id': 'trending-4'},
            {'num': '5', 'target_id': 'trending-5'},
            {'num': '6', 'target_id': 'trending-6'},
        ]
    },
    {
        'doc_name': '[BCTT] Society.docx',
        'cat_folder': 'society',
        'articles': [
            {'num': '2', 'target_id': 'society-1'},
            {'num': '4', 'target_id': 'society-6'},
            {'num': '5', 'target_id': 'society-7'},
            {'num': '6', 'target_id': 'society-8'},
            {'num': '7', 'target_id': 'society-9'},
        ]
    },
    {
        'doc_name': '[BCTT] Human stories.docx',
        'cat_folder': 'human_stories',
        'articles': [
            {'num': '1', 'target_id': 'human-1'},
            {'num': '2', 'target_id': 'human-2'},
            {'num': '3', 'target_id': 'human-3'},
            {'num': '5_farmers', 'target_id': 'human-4'},
            {'num': '5_landmines', 'target_id': 'human-5'},
            {'num': '8_wheelchair', 'target_id': 'human-9'},
            {'num': '8_electricity', 'target_id': 'human-10'},
        ]
    },
    {
        'doc_name': '[BCTT] Mind & Soul.docx',
        'cat_folder': 'mind_&_soul',
        'articles': [
            {'num': '1', 'target_id': 'mind-1'},
            {'num': '2', 'target_id': 'mind-2'},
            {'num': '3', 'target_id': 'mind-3'},
            {'num': '5', 'target_id': 'mind-5'},
            {'num': '6', 'target_id': 'mind-7'},
        ]
    },
    {
        'doc_name': '[BCTT] In-dept.docx',
        'cat_folder': 'in-dept',
        'articles': [
            {'num': '1', 'target_id': 'indepth-1'},
            {'num': '2', 'target_id': 'indepth-2'},
            {'num': '3', 'target_id': 'indepth-3'},
            {'num': '4', 'target_id': 'indepth-4'},
            {'num': '5', 'target_id': 'indepth-5'},
        ]
    }
]

print("Setup parsed correctly.")
