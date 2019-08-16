

def leave_form_message():
    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Request leave",
                    "emoji": True
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a leave type",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Vacation",
                                    "emoji": True
                                },
                                "value": "vacation"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Sick",
                                    "emoji": True
                                },
                                "value": "sick"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Paternity",
                                    "emoji": True
                                },
                                "value": "paternity"
                            }
                        ]
                    },
                    {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select period",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "One day",
                                    "emoji": True
                                },
                                "value": "one-day"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Half day",
                                    "emoji": True
                                },
                                "value": "half-day"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Range",
                                    "emoji": True
                                },
                                "value": "range"
                            }
                        ]
                    },
                    {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select date",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Aug 07, 2019",
                                    "emoji": True
                                },
                                "value": "08-07-2019"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Aug 08, 2019",
                                    "emoji": True
                                },
                                "value": "08-08-2019"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Aug 09, 2019",
                                    "emoji": True
                                },
                                "value": "08-09-2019"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "File Request Leave",
                            "emoji": True
                        },
                        "style": "primary",
                        "value": "request_leave"
                    }
                ]
            }
        ]
    }

    return message

def approval_form_message():
    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "You have a new leave request:\n*<google.com|Richmond Gozarin - Time Off request>*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Type:* Vacation \n*When:* Aug 10-Aug 13\n*Hours:* 16.0 (2 days)\n*Reason:* \"Family in town, going camping!\""
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://api.slack.com/img/blocks/bkb_template_images/approvalsNewDevice.png",
                    "alt_text": "computer thumbnail"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Approve"
                        },
                        "style": "primary",
                        "value": "approved"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Deny"
                        },
                        "style": "danger",
                        "value": "denied"
                    }
                ]
            }
        ]
    }

    return message


def my_leaves_message(data: list):
    TITLE = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*My Leaves*"
                }
            }

    ACTION_BUTTONS = {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Cancel"
                },
                "style": "danger",
                "value": "cancel_leave"
            }
        ]
    }
    
    
    message = {
        "blocks": []
    }

    for field in data:
        FIELDS = {
            "type": "section",
            "fields": []
        }
        
        message['blocks'].append(TITLE)
        leave_record = [
            {
                "type": "mrkdwn",
                "text": "*Leave Type:*\n Vacation"
            },
            {
                "type": "mrkdwn",
                "text": "*Approver:*\n %s" % field['approver']
            },
            {
                "type": "mrkdwn",
                "text": "*When:*\n %s - %s" % (field['start_date'], field['end_date'])
            }
        ]
        
        FIELDS['fields'] = leave_record
        message['blocks'].append(FIELDS)
        
        message['blocks'].append(ACTION_BUTTONS)

    

    return message
    

def default_message():
    return {
        "response_type": "ephemeral",
        "text": "Sorry, that didn't work. Please try again."
    }
