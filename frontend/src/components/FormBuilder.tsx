import React, { useState } from 'react'
import { useForm } from 'react-hook-form'

interface Question {
  id: number
  label: string
  type: string
  options?: string
}

interface FormValues {
  name: string
}

const QUESTION_TYPES = ['text', 'select', 'rating', 'boolean'] as const

const FormBuilder: React.FC = () => {
  const { register, handleSubmit, reset } = useForm<FormValues>()
  const [questions, setQuestions] = useState<Question[]>([])

  const addQuestion = () => {
    setQuestions(prev => [...prev, { id: Date.now(), label: '', type: 'text', options: '' }])
  }

  const updateQuestion = (id: number, field: keyof Question, value: string) => {
    setQuestions(prev => prev.map(q => (q.id === id ? { ...q, [field]: value } : q)))
  }

  const removeQuestion = (id: number) => {
    setQuestions(prev => prev.filter(q => q.id !== id))
  }

  const onSubmit = async (data: FormValues) => {
    if (!data.name.trim()) {
      alert('Form name is required')
      return
    }
    if (questions.some(q => !q.label.trim())) {
      alert('All questions must have a label')
      return
    }

    const payload = {
      name: data.name,
      questions: questions.map(q => ({
        label: q.label,
        type: q.type,
        options: q.options
          ? q.options.split(',').map(o => o.trim()).filter(Boolean)
          : undefined,
      })),
    }

    try {
      const res = await fetch(import.meta.env.VITE_BACKEND_URL + '/forms', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
      const result = await res.json()
      reset()
      setQuestions([])
      alert(`Form saved with ID: ${result.id}`)
    } catch (err) {
      console.error(err)
      alert('Error saving form')
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <div>
        <label>
          Form Name:
          <input {...register('name', { required: true })} />
        </label>
      </div>

      <h2>Questions</h2>
      {questions.map(q => (
        <div key={q.id} style={{ marginBottom: '1rem' }}>
          <input
            type="text"
            placeholder="Question label"
            value={q.label}
            onChange={e => updateQuestion(q.id, 'label', e.target.value)}
          />
          <select
            value={q.type}
            onChange={e => updateQuestion(q.id, 'type', e.target.value)}
          >
            {QUESTION_TYPES.map(t => (
              <option key={t} value={t}>
                {t}
              </option>
            ))}
          </select>
          {q.type === 'select' && (
            <input
              type="text"
              placeholder="Option1, Option2"
              value={q.options}
              onChange={e => updateQuestion(q.id, 'options', e.target.value)}
            />
          )}
          <button type="button" onClick={() => removeQuestion(q.id)}>
            Remove
          </button>
        </div>
      ))}

      <button type="button" onClick={addQuestion}>
        Add Question
      </button>

      <div style={{ marginTop: '1rem' }}>
        <button type="submit">Save Form</button>
      </div>
    </form>
  )
}

export default FormBuilder
