from abc import ABC, abstractmethod
from datetime import datetime
from date.date_provider_service import DateProviderService
from greeting.greeting_provider_service import GreetingProviderService
from log.get_logger import get_logger


LOG = get_logger("greeting.GreetingProviderServiceImpl")
class GreetingProviderServiceImpl(GreetingProviderService):
  def __init__(self, date_provider_service: DateProviderService):
      self.date_provider_service = date_provider_service

  def _is_morning_afternoon_or_evening(self) -> bool: 
    now: datetime = self.date_provider_service.get_now()
    hour = now.hour
    LOG.debug(f"The hour is {hour}")
    
    if hour < 12:
        return "morning"
    elif hour < 17:
        return "afternoon"
    else:
        return "evening"   


  def get_greeting(self) -> str:
    return f"Good {self._is_morning_afternoon_or_evening()}"
      