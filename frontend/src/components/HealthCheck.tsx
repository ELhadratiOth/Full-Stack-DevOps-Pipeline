import React, { useEffect, useState } from 'react'
import { healthApi } from '../services/api'

export const HealthCheck: React.FC = () => {
  const [status, setStatus] = useState<string>('checking...')
  const [isHealthy, setIsHealthy] = useState<boolean>(false)

  useEffect(() => {
    const checkHealth = async () => {
      try {
        const response = await healthApi.check()
        setStatus(response.status || 'healthy')
        setIsHealthy(true)
      } catch (error) {
        setStatus('unhealthy')
        setIsHealthy(false)
      }
    }

    checkHealth()
    const interval = setInterval(checkHealth, 30000) // Check every 30 seconds
    return () => clearInterval(interval)
  }, [])

  return (
    <div className={`p-4 rounded-lg ${isHealthy ? 'bg-green-50 border border-green-200' : 'bg-red-50 border border-red-200'}`}>
      <h3 className="text-sm font-medium text-gray-900">API Health</h3>
      <p className={`text-sm mt-1 ${isHealthy ? 'text-green-700' : 'text-red-700'}`}>
        Status: {status}
      </p>
    </div>
  )
}
