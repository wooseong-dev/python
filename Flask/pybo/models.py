
#모든 모델의 기본 클래스인 db.Model을 상속받음
from pybo import db

class Questioin(db.Model):
    id = db.Column(db.Integer, primary_key = True) #id는 primary_key 주요키로 설정, (데이터 타입 지정, 기본 키로 지정) id는 고유 번호로 중복되면 안되기에 primary_key 옵션을 사용함
    subject = db.Column(db.String(200), nullable=False) # string형
    content = db.Column(db.Text(), nullable=False) # text 형
    create_date = db.Column(db.DateTime(), nullable=False) # 날짜형
    
class Answer(db.Model):
    id = db.Column(db.integer, primary_key=True)# 이 역시 id는 고유번호이기 때문에 기본키로 설정
    question_id = db.Column(db.integer, db.ForeignKey('question_id', ondelete='CASCADE'))# 질문모델과 연결하기 위해 사용 어떤 속성을 기존 모델과 연결하려면 foreignkey를 사용해야함
    # db.ForeignKey(연결할 기존 모델 속성, 삭제 연동 설정)
    #삭제 연동 설정이란 질문 삭제시 question_id 도 삭제됨을 의미
    content = db.Column(db.Text(), nullable=False)
    create_date=db.Column(db.DateTime(), nullable=False)
    
    '''
    question = db.relationship('Question', backref=db.backref('answer_set'))
                기존 모델 참조    참조 모델
                
    backref는 역참조 설정 즉 질문에서 답변을 참조
    질문에 해당하는 객체가 a_question이면 a_question.answer_set을 통해 해당 질문에 달린 답변을 참조 가능
'''
    
    '''
    a_question.delete() -> 질문 데이터 삭제시 해당 질문과 연관된 답변 데이터는 삭제되지 않고 답변 데이터의
    question_id 컬럼만 빈값으로 업데이트 된다.
    
    만약 질문 삭제시 답변까지 삭제되길 바란다면
    db.backref('answer_set', cascade='all, delete-orphan') 로 옵션 추가해야 함
    
    '''