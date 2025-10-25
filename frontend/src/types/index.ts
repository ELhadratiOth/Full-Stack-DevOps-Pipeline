export interface User {
  id: number
  name: string
  email: string
  active: boolean
}

export interface Product {
  id: number
  name: string
  description: string
  price: number
  in_stock: boolean
}

export interface ApiResponse<T> {
  data?: T
  error?: string
  message?: string
}
