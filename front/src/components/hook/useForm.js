import { useState } from 'react'
import { useDispatch } from 'react-redux'

export const useForm = () => {
  const [form, setForm] = useState({})
  const dispatch = useDispatch()

  const onChange = (e) => {
    e.preventDefault()

    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const onSet = (e, func) => {
    e.preventDefault()

    dispatch(func(form))
    setForm({})
  }

  return { form, setForm, onChange, onSet }
}
