import React from 'react'
import { User } from '../types'

interface UserCardProps {
  user: User
}

export const UserCard: React.FC<UserCardProps> = ({ user }) => {
  return (
    <div className="p-4 border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition">
      <h3 className="text-lg font-semibold text-gray-900">{user.name}</h3>
      <p className="text-sm text-gray-600">{user.email}</p>
      <p className="mt-2 text-xs">
        <span className={`px-2 py-1 rounded ${user.active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
          {user.active ? 'Active' : 'Inactive'}
        </span>
      </p>
    </div>
  )
}
