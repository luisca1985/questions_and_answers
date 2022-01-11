export interface Answer {
    id: number;
    question_to_answer: number;
    answered_by: number;
    detail: string;
    is_correct: boolean;
    created: Date;
    modified: Date;
}