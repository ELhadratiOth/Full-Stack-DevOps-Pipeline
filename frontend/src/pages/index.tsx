import React from 'react'
import { HealthCheck } from '../components/HealthCheck'

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4">
          <h1 className="text-3xl font-bold text-gray-900">Microservice Dashboard</h1>
          <p className="text-gray-600 mt-2">Testing & Automation Example</p>
        </div>
      </header>

      <main className="max-w-7xl mx-auto py-12 px-4">
        <div className="mb-8">
          <HealthCheck />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <section className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Users Management</h2>
            <p className="text-gray-600 mb-4">Manage users through the API</p>
            <a href="/users" className="inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
              View Users
            </a>
          </section>

          <section className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Products Management</h2>
            <p className="text-gray-600 mb-4">Manage products through the API</p>
            <a href="/products" className="inline-block bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
              View Products
            </a>
          </section>
        </div>

        <section className="mt-12 bg-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">API Documentation</h2>
          <p className="text-gray-600 mb-4">
            Access the interactive API documentation at:
          </p>
          <ul className="space-y-2">
            <li>
              <a href="http://localhost:8000/docs" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                Swagger UI: http://localhost:8000/docs
              </a>
            </li>
            <li>
              <a href="http://localhost:8000/redoc" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                ReDoc: http://localhost:8000/redoc
              </a>
            </li>
          </ul>
        </section>
      </main>
    </div>
  )
}
