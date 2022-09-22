# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timesheet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import weladee_pb2 as weladee__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftimesheet.proto\x12\x10grpc.weladee.com\x1a\rweladee.proto\"q\n\x11ShareSheetRequest\x12\r\n\x05Token\x18\x01 \x01(\t\x12\x11\n\tProjectID\x18\n \x01(\x03\x12\x0e\n\x06TaskID\x18\x14 \x01(\x03\x12\x0c\n\x04\x46rom\x18\x1e \x01(\x03\x12\n\n\x02To\x18  \x01(\x03\x12\x10\n\x08Language\x18( \x01(\t\"\xc9\x01\n\x0bSharedSheet\x12\x13\n\x0b\x43ompanyName\x18\x02 \x01(\t\x12\x13\n\x0b\x43ompanyLogo\x18\x03 \x01(\t\x12\x14\n\x0c\x43ustomerName\x18\x05 \x01(\t\x12\x14\n\x0c\x43ustomerLogo\x18\x06 \x01(\t\x12\x18\n\x10ShowTimeToCharge\x18\x08 \x01(\x08\x12\x12\n\nShowLocked\x18\t \x01(\x08\x12\'\n\x06Sheets\x18\n \x03(\x0b\x32\x17.grpc.weladee.com.Sheet\x12\r\n\x05\x44\x65lay\x18\x1e \x01(\x05\"X\n\x16\x45mployeeProjectRequest\x12\x1e\n\nEmployeeID\x18\x01 \x01(\x03R\nemployeeid\x12\x1e\n\nCustomerID\x18\x02 \x01(\x03R\ncustomerid\"S\n\x13\x45mployeeTaskRequest\x12\x1e\n\nEmployeeID\x18\x01 \x01(\x03R\nemployeeid\x12\x1c\n\tProjectID\x18\x02 \x01(\x03R\tprojectid\"\xe0\x04\n\x0cSheetRequest\x12\x0e\n\x02ID\x18\x02 \x01(\x03R\x02id\x12\x1e\n\nEmployeeID\x18\x04 \x01(\x03R\nemployeeid\x12\x1c\n\tProjectID\x18\n \x01(\x03R\tprojectid\x12\x12\n\x04\x46rom\x18\x07 \x01(\x05R\x04\x66rom\x12\x0e\n\x02To\x18\x08 \x01(\x05R\x02to\x12\x16\n\x06TaskID\x18\x03 \x01(\x03R\x06taskid\x12\x1f\n\nWorkTypeID\x18\t \x01(\x03R\x0bwork_typeid\x12\x1e\n\nCustomerID\x18\x05 \x01(\x03R\ncustomerid\x12\x31\n\x06Locked\x18\x12 \x01(\x0e\x32\x19.grpc.weladee.com.TrinaryR\x06locked\x12\x10\n\x03XLS\x18\x13 \x01(\x08R\x03xls\x12\x16\n\x06TeamID\x18\x14 \x01(\x03R\x06teamid\x12\x1b\n\x08TeamName\x18\x1e \x01(\tR\tteam_name\x12#\n\x0c\x45mployeeName\x18\x1f \x01(\tR\remployee_name\x12\x1b\n\x08TaskName\x18  \x01(\tR\ttask_name\x12!\n\x0bProjectName\x18! \x01(\tR\x0cproject_name\x12#\n\x0c\x43ustomerName\x18\" \x01(\tR\rcustomer_name\x12!\n\x0bProjectCode\x18# \x01(\tR\x0cproject_code\x12\x1b\n\x08TaskCode\x18$ \x01(\tR\ttask_code\x12\x1b\n\x08LockedBy\x18% \x01(\x03R\tlocked_by\x12$\n\x0cWorkTypeName\x18( \x01(\tR\x0ework_type_name\"\x96\x08\n\x05Sheet\x12\x0e\n\x02ID\x18\x02 \x01(\x03R\x02id\x12\x16\n\x06TaskID\x18\x03 \x01(\x03R\x06taskid\x12\x1e\n\nEmployeeID\x18\x04 \x01(\x03R\nemployeeid\x12\x1e\n\nCustomerID\x18\x01 \x01(\x03R\ncustomerid\x12\x1c\n\tProjectID\x18\n \x01(\x03R\tprojectid\x12\x1f\n\nWorkTypeID\x18\t \x01(\x03R\x0bwork_typeid\x12\x16\n\x06locked\x18\x05 \x01(\x08R\x06locked\x12\x1d\n\tTimeSpent\x18\x06 \x01(\x05R\ntime_spent\x12\x10\n\x03\x44\x61y\x18\x07 \x01(\x05R\x03\x64\x61y\x12 \n\x0b\x44\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12\x18\n\x07Weekday\x18\x0e \x01(\rR\x07weekday\x12\x12\n\x04Note\x18\x0b \x01(\tR\x04note\x12\x12\n\x04\x46rom\x18\x0c \x01(\tR\x04\x66rom\x12\x0e\n\x02To\x18\r \x01(\tR\x02to\x12$\n\x0cTimeToCharge\x18\x33 \x01(\x05R\x0etime_to_charge\x12\x12\n\x04\x43ost\x18. \x01(\x01R\x04\x63ost\x12#\n\x0c\x45mployeeName\x18\x13 \x01(\tR\remployee_name\x12\x1b\n\x08TeamName\x18\x1d \x01(\tR\tteam_name\x12#\n\x0c\x43ustomerName\x18\x17 \x01(\tR\rcustomer_name\x12!\n\x0bProjectName\x18\x14 \x01(\tR\x0cproject_name\x12\x1b\n\x08TaskName\x18\x15 \x01(\tR\ttask_name\x12$\n\x0cWorkTypeName\x18\x16 \x01(\tR\x0ework_type_name\x12!\n\x0bProjectCode\x18\x18 \x01(\tR\x0cproject_code\x12\x1b\n\x08TaskCode\x18\x19 \x01(\tR\ttask_code\x12$\n\x0cWorkTypeCode\x18\x1a \x01(\tR\x0ework_type_code\x12#\n\x0c\x45mployeeCode\x18\x1b \x01(\tR\remployee_code\x12\x1b\n\x08LockedBy\x18$ \x01(\x03R\tlocked_by\x12\x1b\n\x08LockedOn\x18% \x01(\x03R\tlocked_on\x12/\n\x12ProjectDescription\x18& \x01(\tR\x13project_description\x12)\n\x0fTaskDescription\x18\' \x01(\tR\x10task_description\x12\x1f\n\nProjectURL\x18( \x01(\tR\x0bproject_url\x12\x19\n\x07TaskURL\x18) \x01(\tR\x08task_url\x12$\n\x0cLockedByName\x18- \x01(\tR\x0elocked_by_name\x12\x1f\n\nTaskStatus\x18\x32 \x01(\rR\x0btask_status\"\x90\x04\n\tSheetStat\x12\x16\n\x06TaskID\x18\x03 \x01(\x03R\x06taskid\x12\x1e\n\nEmployeeID\x18\x04 \x01(\x03R\nemployeeid\x12\x1e\n\nCustomerID\x18\x01 \x01(\x03R\ncustomerid\x12\x1c\n\tProjectID\x18\n \x01(\x03R\tprojectid\x12\x1f\n\nWorkTypeID\x18\t \x01(\x03R\x0bwork_typeid\x12\x1d\n\tTimeSpent\x18\x06 \x01(\x05R\ntime_spent\x12#\n\x0c\x45mployeeName\x18\x13 \x01(\tR\remployee_name\x12#\n\x0c\x43ustomerName\x18\x17 \x01(\tR\rcustomer_name\x12!\n\x0bProjectName\x18\x14 \x01(\tR\x0cproject_name\x12\x1b\n\x08TaskName\x18\x15 \x01(\tR\ttask_name\x12$\n\x0cWorkTypeName\x18\x16 \x01(\tR\x0ework_type_name\x12!\n\x0bProjectCode\x18\x18 \x01(\tR\x0cproject_code\x12\x1b\n\x08TaskCode\x18\x19 \x01(\tR\ttask_code\x12$\n\x0cWorkTypeCode\x18\x1a \x01(\tR\x0ework_type_code\x12#\n\x0c\x45mployeeCode\x18\x1b \x01(\tR\remployee_code\x12\x12\n\x04\x43ost\x18\x1e \x01(\x01R\x04\x63ost\"\x8a\x03\n\x08\x43ustomer\x12\x0e\n\x02ID\x18\x02 \x01(\x03R\x02id\x12!\n\x0bNameEnglish\x18\x03 \x01(\tR\x0cname_english\x12\x1b\n\x08NameThai\x18\x04 \x01(\tR\tname_thai\x12\x16\n\x06\x61\x63tive\x18\x05 \x01(\x08R\x06\x61\x63tive\x12\x12\n\x04\x43ode\x18\x08 \x01(\tR\x04\x63ode\x12\x12\n\x04Note\x18\x06 \x01(\tR\x04note\x12\x14\n\x08Language\x18\x07 \x01(\tR\x02lg\x12\x14\n\x05\x45mail\x18\t \x01(\tR\x05\x65mail\x12\x18\n\x07\x61\x64\x64ress\x18\n \x01(\tR\x07\x61\x64\x64ress\x12\x12\n\x04\x63ity\x18\x0b \x01(\tR\x04\x63ity\x12\x1a\n\x08postcode\x18\x0c \x01(\tR\x08postcode\x12\x18\n\x07\x63ountry\x18\r \x01(\tR\x07\x63ountry\x12\x10\n\x03URL\x18\x0e \x01(\tR\x03url\x12\x12\n\x04Logo\x18\x12 \x01(\tR\x04logo\x12\x1a\n\x08Latitude\x18\x15 \x01(\x01R\x08latitude\x12\x1c\n\tLongitude\x18\x16 \x01(\x01R\tlongitude\"\xd6\x01\n\x05Stage\x12\x0e\n\x02ID\x18\x01 \x01(\x03R\x02id\x12\x14\n\x05Order\x18\x02 \x01(\rR\x05order\x12!\n\x0bNameEnglish\x18\x04 \x01(\tR\x0cname_english\x12\x1b\n\x08NameThai\x18\x05 \x01(\tR\tname_thai\x12\x14\n\x05\x43olor\x18\x06 \x01(\tR\x05\x63olor\x12\x16\n\x06\x61\x63tive\x18\x07 \x01(\x08R\x06\x61\x63tive\x12\x12\n\x04Note\x18\x08 \x01(\tR\x04note\x12%\n\rFillTimeSheet\x18\n \x01(\x08R\x0e\x66ill_timesheet\"\xf6\x04\n\x07Project\x12\x0e\n\x02ID\x18\x02 \x01(\x03R\x02id\x12!\n\x0bNameEnglish\x18\x03 \x01(\tR\x0cname_english\x12\x1b\n\x08NameThai\x18\x04 \x01(\tR\tname_thai\x12\x12\n\x04\x43ode\x18\x08 \x01(\tR\x04\x63ode\x12\x1e\n\nCustomerID\x18\x05 \x01(\x03R\ncustomerid\x12\x16\n\x06\x61\x63tive\x18\x06 \x01(\x08R\x06\x61\x63tive\x12\x12\n\x04Note\x18\x07 \x01(\tR\x04note\x12\x10\n\x03URL\x18\x0e \x01(\tR\x03url\x12/\n\x12\x44\x65scriptionEnglish\x18\x0f \x01(\tR\x13\x64\x65scription_english\x12)\n\x0f\x44\x65scriptionThai\x18\x10 \x01(\tR\x10\x64\x65scription_thai\x12\x32\n\x13\x43ustomerNameEnglish\x18\x14 \x01(\tR\x15\x63ustomer_name_english\x12,\n\x10\x43ustomerNameThai\x18\x15 \x01(\tR\x12\x63ustomer_name_thai\x12\x42\n\x1a\x44\x65\x66\x61ultWorkTypeNameEnglish\x18\x16 \x01(\tR\x1e\x64\x65\x66\x61ult_work_type_name_english\x12<\n\x17\x44\x65\x66\x61ultWorkTypeNameThai\x18\x17 \x01(\tR\x1b\x64\x65\x66\x61ult_work_type_name_thai\x12.\n\x11\x44\x65\x66\x61ultWorkTypeID\x18\t \x01(\x03R\x13\x64\x65\x66\x61ult_work_typeid\x12#\n\x0c\x43ustomerLogo\x18\x1e \x01(\tR\rcustomer_logo\x12\x14\n\x05Score\x18P \x01(\rR\x05score\"\x8e\x07\n\x04Task\x12\x0e\n\x02ID\x18\x02 \x01(\x03R\x02id\x12!\n\x0bNameEnglish\x18\x03 \x01(\tR\x0cname_english\x12\x1b\n\x08NameThai\x18\x04 \x01(\tR\tname_thai\x12\x1c\n\tProjectID\x18\x05 \x01(\x03R\tprojectid\x12\x16\n\x06\x61\x63tive\x18\x06 \x01(\x08R\x06\x61\x63tive\x12\x16\n\x06Status\x18\x07 \x01(\rR\x06status\x12\x12\n\x04\x43ode\x18\x08 \x01(\tR\x04\x63ode\x12\x12\n\x04Note\x18\t \x01(\tR\x04note\x12.\n\x11\x44\x65\x66\x61ultWorkTypeID\x18\n \x01(\x03R\x13\x64\x65\x66\x61ult_work_typeid\x12\x1e\n\nCustomerID\x18\x0b \x01(\x03R\ncustomerid\x12\x10\n\x03URL\x18\x0e \x01(\tR\x03url\x12/\n\x12\x44\x65scriptionEnglish\x18\x0f \x01(\tR\x13\x64\x65scription_english\x12)\n\x0f\x44\x65scriptionThai\x18\x10 \x01(\tR\x10\x64\x65scription_thai\x12\x30\n\x12ProjectNameEnglish\x18\x14 \x01(\tR\x14project_name_english\x12*\n\x0fProjectNameThai\x18\x15 \x01(\tR\x11project_name_thai\x12,\n\x10\x43ustomerNameThai\x18\x16 \x01(\tR\x12\x63ustomer_name_thai\x12\x32\n\x13\x43ustomerNameEnglish\x18\x17 \x01(\tR\x15\x63ustomer_name_english\x12\x1a\n\x08\x44\x65\x61\x64line\x18\x19 \x01(\x05R\x08\x64\x65\x61\x64line\x12\x1e\n\nEstimation\x18\x1a \x01(\rR\nestimation\x12\x42\n\x1a\x44\x65\x66\x61ultWorkTypeNameEnglish\x18\x1e \x01(\tR\x1e\x64\x65\x66\x61ult_work_type_name_english\x12<\n\x17\x44\x65\x66\x61ultWorkTypeNameThai\x18\x1f \x01(\tR\x1b\x64\x65\x66\x61ult_work_type_name_thai\x12\x18\n\x07StageID\x18( \x01(\x03R\x07stageid\x12\x14\n\x05Score\x18P \x01(\rR\x05score\x12,\n\x10StageNameEnglish\x18x \x01(\tR\x12stage_name_english\x12&\n\rStageNameThai\x18y \x01(\tR\x0fstage_name_thai\"\x9a\x01\n\x08WorkType\x12\x0e\n\x02ID\x18\x02 \x01(\x03R\x02id\x12!\n\x0bNameEnglish\x18\x03 \x01(\tR\x0cname_english\x12\x1b\n\x08NameThai\x18\x04 \x01(\tR\tname_thai\x12\x12\n\x04\x43ode\x18\x08 \x01(\tR\x04\x63ode\x12\x16\n\x06\x61\x63tive\x18\x06 \x01(\x08R\x06\x61\x63tive\x12\x12\n\x04Note\x18\t \x01(\tR\x04note\"F\n\x0cTaskEmployee\x12\x1e\n\nEmployeeID\x18\x01 \x01(\x03R\nemployeeid\x12\x16\n\x06TaskID\x18\x02 \x01(\x03R\x06taskid\"O\n\x0fProjectEmployee\x12\x1e\n\nEmployeeID\x18\x01 \x01(\x03R\nemployeeid\x12\x1c\n\tProjectID\x18\x02 \x01(\x03R\tprojectid\"\xbf\x04\n\x14TimeSheetPreferences\x12\x1b\n\x08TaskTime\x18\x01 \x01(\x08R\ttask_time\x12#\n\x0cTaskDeadLine\x18\x02 \x01(\x08R\rtask_deadline\x12\x1f\n\nTaskStatus\x18\x03 \x01(\x08R\x0btask_status\x12,\n\x10SheetSoundRecord\x18\x04 \x01(\x08R\x12sheet_sound_record\x12\x36\n\x15SheetCommentMandatory\x18\x05 \x01(\x08R\x17sheet_comment_mandatory\x12#\n\x0cSheetPicture\x18\x06 \x01(\x08R\rsheet_picture\x12\x14\n\x05Share\x18\x07 \x01(\x08R\x05share\x12/\n\x11ShareTimeToCharge\x18\x08 \x01(\x08R\x14share_time_to_charge\x12\'\n\x0eTaskEstimation\x18\t \x01(\x08R\x0ftask_estimation\x12*\n\x0f\x44\x61ilySheetEmail\x18\n \x01(\rR\x11\x64\x61ily_sheet_email\x12\x14\n\x05Stage\x18\x0b \x01(\x08R\x05stage\x12\'\n\x0eRemindEmployee\x18\x0c \x01(\x08R\x0fremind_employee\x12\x31\n\x13InstructionsEnglish\x18\x14 \x01(\tR\x14instructions_english\x12+\n\x10InstructionsThai\x18\x15 \x01(\tR\x11instructions_thai\"K\n\x0bLockRequest\x12\x0c\n\x04year\x18\x01 \x01(\r\x12\r\n\x05month\x18\x02 \x01(\r\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\r\x12\x12\n\nEmployeeID\x18\x04 \x01(\x03\"a\n\x0c\x43heckRequest\x12\x0c\n\x04year\x18\x01 \x01(\r\x12\r\n\x05month\x18\x02 \x01(\r\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\r\x12\x12\n\nEmployeeID\x18\x04 \x01(\x03\x12\x13\n\x0b\x44\x65scription\x18\x05 \x01(\t\"\xc8\x01\n\x0eSheetTimeSpent\x12\x10\n\x03\x44\x61y\x18\x01 \x01(\x03R\x03\x64\x61y\x12\x1d\n\tTimeSpent\x18\x02 \x01(\x03R\ntime_spent\x12\x16\n\x06locked\x18\x03 \x01(\x08R\x06locked\x12\x18\n\x07holiday\x18\x04 \x01(\x08R\x07holiday\x12\x1d\n\tSickLeave\x18\x05 \x01(\x08R\nsick_leave\x12\x34\n\x07\x44\x61yPart\x18\x06 \x01(\x0e\x32\x19.grpc.weladee.com.DayPartR\x08\x64\x61y_part\"\x97\x03\n\x0bTaskRequest\x12\x1e\n\nCustomerID\x18\x01 \x01(\x03R\ncustomerid\x12\x1c\n\tProjectID\x18\x02 \x01(\x03R\tprojectid\x12\x0e\n\x02ID\x18\x03 \x01(\x03R\x02id\x12\x1e\n\nEmployeeID\x18\x04 \x01(\x03R\nemployeeid\x12\x12\n\x04\x43ode\x18\x05 \x01(\tR\x04\x63ode\x12\x31\n\x06\x61\x63tive\x18\n \x01(\x0e\x32\x19.grpc.weladee.com.TrinaryR\x06\x61\x63tive\x12\x0f\n\x07ShareID\x18n \x01(\x03\x12\x18\n\x07StageID\x18q \x01(\x03R\x07stageid\x12\x1d\n\tStageName\x18o \x01(\tR\nstage_name\x12\x1b\n\x08TaskName\x18\x0b \x01(\tR\ttask_name\x12!\n\x0bProjectName\x18\x0c \x01(\tR\x0cproject_name\x12#\n\x0c\x43ustomerName\x18\r \x01(\tR\rcustomer_name\x12\x12\n\x04\x44\x61te\x18\x0e \x01(\rR\x04\x64\x61te\x12\x10\n\x03XLS\x18\x15 \x01(\x08R\x03xls\"F\n\x0cProjectStage\x12\x1c\n\tProjectID\x18\x01 \x01(\x03R\tprojectid\x12\x18\n\x07StageID\x18\x02 \x01(\x03R\x07stageid\"=\n\tTaskStage\x12\x16\n\x06TaskID\x18\x01 \x01(\x03R\x06taskid\x12\x18\n\x07StageID\x18\x02 \x01(\x03R\x07stageid\"\xdb\x01\n\x0cStageRequest\x12\x0e\n\x02ID\x18\x01 \x01(\x03R\x02id\x12\x1c\n\tProjectID\x18\x02 \x01(\x03R\tprojectid\x12\x16\n\x06TaskID\x18\x04 \x01(\x03R\x06taskid\x12\x31\n\x06\x41\x63tive\x18\n \x01(\x0e\x32\x19.grpc.weladee.com.TrinaryR\x06\x61\x63tive\x12\x1d\n\tStageName\x18\x0b \x01(\tR\nstage_name\x12!\n\x0bProjectName\x18\x0c \x01(\tR\x0cproject_name\x12\x10\n\x03XLS\x18\x15 \x01(\x08R\x03xls\"\xa5\x02\n\x0eProjectRequest\x12\x0b\n\x03IDs\x18\x01 \x03(\x03\x12\x38\n\tWithStage\x18\x03 \x01(\x0e\x32\x19.grpc.weladee.com.TrinaryR\nwith_stage\x12)\n\x06\x61\x63tive\x18\x02 \x01(\x0e\x32\x19.grpc.weladee.com.Trinary\x12\x0e\n\x06Offset\x18\t \x01(\x03\x12\r\n\x05Limit\x18\n \x01(\x03\x12\x0c\n\x04\x43ode\x18\x0c \x01(\t\x12\x0f\n\x07ShareID\x18\x07 \x01(\x03\x12\x12\n\nEmployeeID\x18\r \x01(\x03\x12\x13\n\x0bProjectName\x18\x12 \x01(\t\x12\x12\n\nCustomerID\x18\x13 \x01(\x03\x12\x14\n\x0c\x43ustomerName\x18\x14 \x01(\t\x12\x10\n\x03XLS\x18\x15 \x01(\x08R\x03xls\";\n\x08NewSheet\x12\x0c\n\x04\x44\x61te\x18\x01 \x01(\x05\x12\x11\n\tProjectID\x18\x02 \x01(\x03\x12\x0e\n\x06TaskID\x18\x03 \x01(\x03\"\x96\x03\n\x05Share\x12\x1c\n\tCompanyID\x18\x01 \x01(\x03R\tcompanyid\x12\x0e\n\x02ID\x18\x02 \x01(\x03R\x02id\x12!\n\x0bNameEnglish\x18\x03 \x01(\tR\x0cname_english\x12\x1b\n\x08NameThai\x18\x04 \x01(\tR\tname_thai\x12\x16\n\x06\x61\x63tive\x18\x06 \x01(\x08R\x06\x61\x63tive\x12/\n\x11ShareTimeToCharge\x18\x08 \x01(\x08R\x14share_time_to_charge\x12\x12\n\x04Note\x18\t \x01(\tR\x04note\x12\x1e\n\nCustomerID\x18\x0b \x01(\x03R\ncustomerid\x12#\n\x0c\x43ustomerName\x18\x0c \x01(\tR\rcustomer_name\x12\x10\n\x03URL\x18\x0e \x01(\tR\x03url\x12\x12\n\x04\x46rom\x18\x32 \x01(\x03R\x04\x66rom\x12\x0e\n\x02To\x18\x34 \x01(\x03R\x02to\x12\x14\n\x05\x44\x65lay\x18\x36 \x01(\x05R\x05\x64\x65lay\x12\x31\n\x06Locked\x18< \x01(\x0e\x32\x19.grpc.weladee.com.TrinaryR\x06locked\"F\n\x0cProjectShare\x12\x1c\n\tProjectID\x18\x01 \x01(\x03R\tprojectid\x12\x18\n\x07ShareID\x18\x02 \x01(\x03R\x07shareid\"=\n\tTaskShare\x12\x16\n\x06TaskID\x18\x01 \x01(\x03R\x06taskid\x12\x18\n\x07ShareID\x18\x02 \x01(\x03R\x07shareid\"\x9b\x01\n\x0cShareRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\x12)\n\x06\x61\x63tive\x18\x02 \x01(\x0e\x32\x19.grpc.weladee.com.Trinary\x12\x0e\n\x06Offset\x18\t \x01(\x03\x12\r\n\x05Limit\x18\n \x01(\x03\x12\x12\n\nCustomerID\x18\x13 \x01(\x03\x12\x14\n\x0c\x43ustomerName\x18\x14 \x01(\t\x12\x0b\n\x03XLS\x18\x15 \x01(\x08\x32`\n\tTimeSheet\x12S\n\rGetTimeSheets\x12#.grpc.weladee.com.ShareSheetRequest\x1a\x1d.grpc.weladee.com.SharedSheetB5\n\x1f\x63om.frontware.weladee_timesheetB\x0bWeladeeGRPCH\x03P\x01\x90\x01\x01\x62\x06proto3')



_SHARESHEETREQUEST = DESCRIPTOR.message_types_by_name['ShareSheetRequest']
_SHAREDSHEET = DESCRIPTOR.message_types_by_name['SharedSheet']
_EMPLOYEEPROJECTREQUEST = DESCRIPTOR.message_types_by_name['EmployeeProjectRequest']
_EMPLOYEETASKREQUEST = DESCRIPTOR.message_types_by_name['EmployeeTaskRequest']
_SHEETREQUEST = DESCRIPTOR.message_types_by_name['SheetRequest']
_SHEET = DESCRIPTOR.message_types_by_name['Sheet']
_SHEETSTAT = DESCRIPTOR.message_types_by_name['SheetStat']
_CUSTOMER = DESCRIPTOR.message_types_by_name['Customer']
_STAGE = DESCRIPTOR.message_types_by_name['Stage']
_PROJECT = DESCRIPTOR.message_types_by_name['Project']
_TASK = DESCRIPTOR.message_types_by_name['Task']
_WORKTYPE = DESCRIPTOR.message_types_by_name['WorkType']
_TASKEMPLOYEE = DESCRIPTOR.message_types_by_name['TaskEmployee']
_PROJECTEMPLOYEE = DESCRIPTOR.message_types_by_name['ProjectEmployee']
_TIMESHEETPREFERENCES = DESCRIPTOR.message_types_by_name['TimeSheetPreferences']
_LOCKREQUEST = DESCRIPTOR.message_types_by_name['LockRequest']
_CHECKREQUEST = DESCRIPTOR.message_types_by_name['CheckRequest']
_SHEETTIMESPENT = DESCRIPTOR.message_types_by_name['SheetTimeSpent']
_TASKREQUEST = DESCRIPTOR.message_types_by_name['TaskRequest']
_PROJECTSTAGE = DESCRIPTOR.message_types_by_name['ProjectStage']
_TASKSTAGE = DESCRIPTOR.message_types_by_name['TaskStage']
_STAGEREQUEST = DESCRIPTOR.message_types_by_name['StageRequest']
_PROJECTREQUEST = DESCRIPTOR.message_types_by_name['ProjectRequest']
_NEWSHEET = DESCRIPTOR.message_types_by_name['NewSheet']
_SHARE = DESCRIPTOR.message_types_by_name['Share']
_PROJECTSHARE = DESCRIPTOR.message_types_by_name['ProjectShare']
_TASKSHARE = DESCRIPTOR.message_types_by_name['TaskShare']
_SHAREREQUEST = DESCRIPTOR.message_types_by_name['ShareRequest']
ShareSheetRequest = _reflection.GeneratedProtocolMessageType('ShareSheetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHARESHEETREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ShareSheetRequest)
  })
_sym_db.RegisterMessage(ShareSheetRequest)

SharedSheet = _reflection.GeneratedProtocolMessageType('SharedSheet', (_message.Message,), {
  'DESCRIPTOR' : _SHAREDSHEET,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.SharedSheet)
  })
_sym_db.RegisterMessage(SharedSheet)

EmployeeProjectRequest = _reflection.GeneratedProtocolMessageType('EmployeeProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPLOYEEPROJECTREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.EmployeeProjectRequest)
  })
_sym_db.RegisterMessage(EmployeeProjectRequest)

EmployeeTaskRequest = _reflection.GeneratedProtocolMessageType('EmployeeTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPLOYEETASKREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.EmployeeTaskRequest)
  })
_sym_db.RegisterMessage(EmployeeTaskRequest)

SheetRequest = _reflection.GeneratedProtocolMessageType('SheetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHEETREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.SheetRequest)
  })
_sym_db.RegisterMessage(SheetRequest)

Sheet = _reflection.GeneratedProtocolMessageType('Sheet', (_message.Message,), {
  'DESCRIPTOR' : _SHEET,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Sheet)
  })
_sym_db.RegisterMessage(Sheet)

SheetStat = _reflection.GeneratedProtocolMessageType('SheetStat', (_message.Message,), {
  'DESCRIPTOR' : _SHEETSTAT,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.SheetStat)
  })
_sym_db.RegisterMessage(SheetStat)

Customer = _reflection.GeneratedProtocolMessageType('Customer', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMER,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Customer)
  })
_sym_db.RegisterMessage(Customer)

Stage = _reflection.GeneratedProtocolMessageType('Stage', (_message.Message,), {
  'DESCRIPTOR' : _STAGE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Stage)
  })
_sym_db.RegisterMessage(Stage)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Project)
  })
_sym_db.RegisterMessage(Project)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Task)
  })
_sym_db.RegisterMessage(Task)

WorkType = _reflection.GeneratedProtocolMessageType('WorkType', (_message.Message,), {
  'DESCRIPTOR' : _WORKTYPE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.WorkType)
  })
_sym_db.RegisterMessage(WorkType)

TaskEmployee = _reflection.GeneratedProtocolMessageType('TaskEmployee', (_message.Message,), {
  'DESCRIPTOR' : _TASKEMPLOYEE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.TaskEmployee)
  })
_sym_db.RegisterMessage(TaskEmployee)

ProjectEmployee = _reflection.GeneratedProtocolMessageType('ProjectEmployee', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTEMPLOYEE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ProjectEmployee)
  })
_sym_db.RegisterMessage(ProjectEmployee)

TimeSheetPreferences = _reflection.GeneratedProtocolMessageType('TimeSheetPreferences', (_message.Message,), {
  'DESCRIPTOR' : _TIMESHEETPREFERENCES,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.TimeSheetPreferences)
  })
_sym_db.RegisterMessage(TimeSheetPreferences)

LockRequest = _reflection.GeneratedProtocolMessageType('LockRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCKREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.LockRequest)
  })
_sym_db.RegisterMessage(LockRequest)

CheckRequest = _reflection.GeneratedProtocolMessageType('CheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.CheckRequest)
  })
_sym_db.RegisterMessage(CheckRequest)

SheetTimeSpent = _reflection.GeneratedProtocolMessageType('SheetTimeSpent', (_message.Message,), {
  'DESCRIPTOR' : _SHEETTIMESPENT,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.SheetTimeSpent)
  })
_sym_db.RegisterMessage(SheetTimeSpent)

TaskRequest = _reflection.GeneratedProtocolMessageType('TaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _TASKREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.TaskRequest)
  })
_sym_db.RegisterMessage(TaskRequest)

ProjectStage = _reflection.GeneratedProtocolMessageType('ProjectStage', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTSTAGE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ProjectStage)
  })
_sym_db.RegisterMessage(ProjectStage)

TaskStage = _reflection.GeneratedProtocolMessageType('TaskStage', (_message.Message,), {
  'DESCRIPTOR' : _TASKSTAGE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.TaskStage)
  })
_sym_db.RegisterMessage(TaskStage)

StageRequest = _reflection.GeneratedProtocolMessageType('StageRequest', (_message.Message,), {
  'DESCRIPTOR' : _STAGEREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.StageRequest)
  })
_sym_db.RegisterMessage(StageRequest)

ProjectRequest = _reflection.GeneratedProtocolMessageType('ProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ProjectRequest)
  })
_sym_db.RegisterMessage(ProjectRequest)

NewSheet = _reflection.GeneratedProtocolMessageType('NewSheet', (_message.Message,), {
  'DESCRIPTOR' : _NEWSHEET,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.NewSheet)
  })
_sym_db.RegisterMessage(NewSheet)

Share = _reflection.GeneratedProtocolMessageType('Share', (_message.Message,), {
  'DESCRIPTOR' : _SHARE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Share)
  })
_sym_db.RegisterMessage(Share)

ProjectShare = _reflection.GeneratedProtocolMessageType('ProjectShare', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTSHARE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ProjectShare)
  })
_sym_db.RegisterMessage(ProjectShare)

TaskShare = _reflection.GeneratedProtocolMessageType('TaskShare', (_message.Message,), {
  'DESCRIPTOR' : _TASKSHARE,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.TaskShare)
  })
_sym_db.RegisterMessage(TaskShare)

ShareRequest = _reflection.GeneratedProtocolMessageType('ShareRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHAREREQUEST,
  '__module__' : 'timesheet_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ShareRequest)
  })
_sym_db.RegisterMessage(ShareRequest)

_TIMESHEET = DESCRIPTOR.services_by_name['TimeSheet']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.frontware.weladee_timesheetB\013WeladeeGRPCH\003P\001\220\001\001'
  _SHARESHEETREQUEST._serialized_start=52
  _SHARESHEETREQUEST._serialized_end=165
  _SHAREDSHEET._serialized_start=168
  _SHAREDSHEET._serialized_end=369
  _EMPLOYEEPROJECTREQUEST._serialized_start=371
  _EMPLOYEEPROJECTREQUEST._serialized_end=459
  _EMPLOYEETASKREQUEST._serialized_start=461
  _EMPLOYEETASKREQUEST._serialized_end=544
  _SHEETREQUEST._serialized_start=547
  _SHEETREQUEST._serialized_end=1155
  _SHEET._serialized_start=1158
  _SHEET._serialized_end=2204
  _SHEETSTAT._serialized_start=2207
  _SHEETSTAT._serialized_end=2735
  _CUSTOMER._serialized_start=2738
  _CUSTOMER._serialized_end=3132
  _STAGE._serialized_start=3135
  _STAGE._serialized_end=3349
  _PROJECT._serialized_start=3352
  _PROJECT._serialized_end=3982
  _TASK._serialized_start=3985
  _TASK._serialized_end=4895
  _WORKTYPE._serialized_start=4898
  _WORKTYPE._serialized_end=5052
  _TASKEMPLOYEE._serialized_start=5054
  _TASKEMPLOYEE._serialized_end=5124
  _PROJECTEMPLOYEE._serialized_start=5126
  _PROJECTEMPLOYEE._serialized_end=5205
  _TIMESHEETPREFERENCES._serialized_start=5208
  _TIMESHEETPREFERENCES._serialized_end=5783
  _LOCKREQUEST._serialized_start=5785
  _LOCKREQUEST._serialized_end=5860
  _CHECKREQUEST._serialized_start=5862
  _CHECKREQUEST._serialized_end=5959
  _SHEETTIMESPENT._serialized_start=5962
  _SHEETTIMESPENT._serialized_end=6162
  _TASKREQUEST._serialized_start=6165
  _TASKREQUEST._serialized_end=6572
  _PROJECTSTAGE._serialized_start=6574
  _PROJECTSTAGE._serialized_end=6644
  _TASKSTAGE._serialized_start=6646
  _TASKSTAGE._serialized_end=6707
  _STAGEREQUEST._serialized_start=6710
  _STAGEREQUEST._serialized_end=6929
  _PROJECTREQUEST._serialized_start=6932
  _PROJECTREQUEST._serialized_end=7225
  _NEWSHEET._serialized_start=7227
  _NEWSHEET._serialized_end=7286
  _SHARE._serialized_start=7289
  _SHARE._serialized_end=7695
  _PROJECTSHARE._serialized_start=7697
  _PROJECTSHARE._serialized_end=7767
  _TASKSHARE._serialized_start=7769
  _TASKSHARE._serialized_end=7830
  _SHAREREQUEST._serialized_start=7833
  _SHAREREQUEST._serialized_end=7988
  _TIMESHEET._serialized_start=7990
  _TIMESHEET._serialized_end=8086
TimeSheet = service_reflection.GeneratedServiceType('TimeSheet', (_service.Service,), dict(
  DESCRIPTOR = _TIMESHEET,
  __module__ = 'timesheet_pb2'
  ))

TimeSheet_Stub = service_reflection.GeneratedServiceStubType('TimeSheet_Stub', (TimeSheet,), dict(
  DESCRIPTOR = _TIMESHEET,
  __module__ = 'timesheet_pb2'
  ))


# @@protoc_insertion_point(module_scope)
