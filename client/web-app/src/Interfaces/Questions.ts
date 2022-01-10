export interface Question {
    id: number;
    asked_by: number;
    title: string;
    detail: string;
    answers_made: number;
    is_resolved: boolean;
    is_closed: boolean;
    is_public: boolean;
}