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

export interface HealthResponse {
  status: string
  service: string
  version: string
}

export interface ReadinessResponse {
  ready: boolean
  message: string
}
